.DEFAULT_GOAL := install

.PHONY: help
help:
	@grep -E '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: python
python:
	@if command -v pyenv >/dev/null 2>&1; then \
		pyenv install --skip-existing; \
		echo "Using Python $$(pyenv version)"; \
	else \
		echo "Using $$(python --version) ($$(which python))"; \
	fi

.venv:
	python3 -m venv .venv

.PHONY: install
install: python .venv ## Install all dependencies
	.venv/bin/python -m pip install --upgrade pip setuptools
	.venv/bin/python -m pip install --requirement requirements.txt --upgrade
	npm install

.PHONY: clean
clean: ## Remove all dependencies
	rm -fr .venv node_modules
