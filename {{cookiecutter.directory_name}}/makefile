.PHONY: help install lint format pytest mypy mypy-types docs download-structures

help:
	@echo "Available commands:"
	@echo "  install                    Install source code in environment"
	@echo "  install-editable           Install source code in environment in editable mode"
	@echo "  install-all                Install source code in environment and all dependencies"
	@echo "  install-editable-all       Install source code in environment and all dependencies in editable mode"
	@echo "  lint                       Run linters using pre-commit"
	@echo "  format                     Run formatters using pre-commit"
	@echo "  pytest                     Run tests using pytest"
	@echo "  mypy                       Run type-checking using mypy"
	@echo "  mypy-types                 Install missing types using mypy"
	@echo "  docs                       Generate documentation using pdoc"
	@echo "  package                    Builds python package"

install:
	pip install .

install-editable:
	pip install --editable .

install-all:
	pip install ".[all]"

install-editable-all:
	pip install --editable ".[all]"

lint:
	pre-commit run ruff --all-files

format:
	pre-commit run ruff-format --all-files

pytest:
	pytest --cov={{cookiecutter.package_name}} --cov-report=term-missing tests

mypy:
	mypy --ignore-missing-imports src

mypy-types:
	mypy --install-types

docs:
	rm -rf docs
	pdoc src/{{cookiecutter.package_name}} -o docs

.DEFAULT_GOAL := help

package:
	python -m build