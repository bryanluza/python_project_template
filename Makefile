.PHONY: install setup run lint format test clean docs docs-clean docs-apidoc

install:
	uv sync

setup: install
	uv run pre-commit install

run:
	uv run ./app/main.py

lint:
	uv run ruff check .
	uv run mypy .

format:
	uv run ruff format .

test:
	uv run pytest

clean:
	rm -rf __pycache__/ .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -name "*.pyc" -exec rm {} +
	find . -name "*.bak" -exec rm {} +

docs-clean:
	uv run sphinx-build -M clean docs docs/_build

docs: docs-clean
	uv run sphinx-build -M html docs docs/_build

docs-apidoc:
	uv run sphinx-apidoc -o docs app