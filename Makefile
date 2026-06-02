.PHONY: version/get
version/get: ## Get version.
	@uv version | awk '{print $$2}'

.PHONY: version/set
version/set: ## Set version.
	@uv version $(v)
	@make version/commit

.PHONY: version/patch
version/patch: ## Bump patch version.
	@uv version --bump patch
	@make version/commit

.PHONY: version/minor
version/minor: ## Bump minor version.
	@uv version --bump minor
	@make version/commit

.PHONY: version/major
version/major: ## Bump major version.
	@uv version --bump major
	@make version/commit

.PHONY: version/commit
version/commit: ## Commit version.
	@uv lock
	@git add pyproject.toml uv.lock
	@git commit -m "chore: bump v$$(make version/get)"

.PHONY: version/publish
version/publish: ## Create and push git tags.
	@git fetch --tags --force
	@git tag v$$(make version/get)
	@git tag stable -f
	@git push -f --tags
	@git push origin HEAD:refs/heads/release/v$$(make version/get | awk -F. '{print $$1 "." $$2}')

.PHONY: install
install: ## Install all dependencies.
	@make install/all

.PHONY: install/core
install/core: ## Install core dependencies.
	@uv sync

.PHONY: install/all
install/all: ## Install all dependencies.
	@uv sync --all-groups --all-extras

.PHONY: install/dev
install/dev: ## Install dev dependencies.
	@uv sync --group dev

.PHONY: install/test
install/test: ## Install test dependencies.
	@uv sync --group test

.PHONY: gen/sdk
gen/sdk: ## Generate the Griptape Cloud SDK.
	@uv run scripts/gen_sdk.py

.PHONY: lint
lint: ## Lint project.
	@uv run ruff check --fix

.PHONY: format
format: ## Format project.
	@uv run ruff format
	@uv run mdformat .github *.md

.PHONY: fix
fix: ## Fix project.
	@make format
	@uv run ruff check --fix --unsafe-fixes

.PHONY: check
check: check/format check/lint check/types check/spell ## Run all checks.

.PHONY: check/format
check/format:
	@uv run ruff format --check
	@uv run mdformat --check .github *.md

.PHONY: check/lint
check/lint:
	@uv run ruff check

.PHONY: check/types
check/types:
	@uv run pyright .
	
.PHONY: check/spell
check/spell:
	@uv run typos

.DEFAULT_GOAL := help
.PHONY: help
help: ## Print Makefile help text.
	@# Matches targets with a comment in the format <target>: ## <comment>
	@# then formats help output using these values.
	@grep -E '^[a-zA-Z_\/-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; \
		{printf "\033[36m%-12s\033[0m%s\n", $$1, $$2}'