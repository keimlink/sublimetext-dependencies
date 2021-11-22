.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: python
python:
	pyenv install --skip-existing

.venv:
	python3 -m venv .venv

.PHONY: install
install: python .venv ## Install all dependencies
	.venv/bin/python -m pip install --upgrade pip setuptools
	.venv/bin/python -m pip install --requirement requirements.txt --upgrade
	npm install

.PHONY: configuration-sublack
configuration-sublack: ## Generate sublack configuration
	@./configure.py sublack

.PHONY: configuration-sublimelinter
configuration-sublimelinter: ## Generate SublimeLinter configuration
	@./configure.py sublimelinter

.PHONY: clean
clean: ## Remove all dependencies
	rm -fr .venv node_modules
