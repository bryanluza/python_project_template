.PHONY: install setup run lint format test clean docs docs-clean

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
	$(MAKE) -C docs clean

docs: docs-clean
	$(MAKE) -C docs html
