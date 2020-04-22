default: | help

test:  ## run all tests with coverage
	pytest --cov=cuban tests/ && coverage html --omit=venv/*

format:  ## run formatter
	autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive cuban tests && \
	isort -rc cuban tests && \
	black -l 119 cuban tests

format-check:
	black -l 119 --check cuban

help:  ## Show all of tasks
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
