# Cookiecutter Python Project Template

A modern, opinionated Python project template for quick starts. This template helps you bootstrap new Python projects with a sensible directory structure, pre-configured tools, and best practices inspired by the wider Python community.

This template is designed to help start Python projects efficiently, using current best practices for packaging, development workflow, and documentation. It is ideal for learners and hobbyists who want a solid foundation for new Python projects.

## Features

- Cookiecutter-powered scaffolding (customize project name, author, etc.) [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
- Project and dependencies managment with isolated Python environment via [`uv`](https://github.com/astral-sh/uv)
- Testing with [`pytest`](https://pytest.org/)
- Pre-configured linting and formatting with [`ruff`](https://github.com/astral-sh/ruff)
- Type checking via [`mypy`](https://mypy-lang.org/)
- Automated code quality checks with [`pre-commit`](https://pre-commit.com/)
- Documentation generation using [`sphinx`](https://www.sphinx-doc.org/)
- Sensible file and folder structure for app code, tests, and docs
- Example Makefile to simplify common dev tasks
- Standard documentation and config files 

## Project structure

```
my_project/
├── .git/                   # Git repository metadata (managed by git)
├── .venv/                  # Virtual environment (managed by uv)
├── app/                    # Main package directory
├── docs/                   # Sphinx documentation
├── tests/                  # Unit and integration tests
├── .gitignore              # Files/directories to ignore in Git
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .python-version         # Python version (created by uv)
├── CHANGELOG.md            # Project changelog
├── LICENSE                 # Project license
├── Makefile                 # Automate common development tasks
├── pyproject.toml          # Project metadata, dependencies, and tool configurations
├── README.md               # Project description, installation, usage
└── uv.lock                 # Managed by uv
```

## Using This Template

To bootstrap a new project:

```bash
pipx install cookiecutter
cookiecutter gh:bryanluza/python_project_template
```

You’ll be prompted to enter project-specific values (name, author, etc.). All placeholders are automatically replaced throughout the generated files.

**Placeholder locations:**
- pyproject.toml
- LICENSE
- app/main.py
- tests/test_main.py
- docs/config.py

## Development Tooling

- **uv**: Fast dependency and virtual environment management. Handles both development and runtime dependencies.
- **ruff**: Fast Python linter and formatter.
- **pre-commit**: Manages and runs hooks for linting/formatting before each commit.
- **pytest**: Framework for unit and integration testing.
- **mypy**: Static type checking for Python.
- **sphinx**: Documentation generation.

*Note: Tools like `uv`, `cookiecutter`, and `git` are required for development workflow but are not installed as runtime dependencies of your project.*

## Project Dependencies

- **pydantic**: Data validation and settings management using Python type hints.
- **pydantic-settings**: Loads environment variables from `.env` files and other sources into Pydantic models.

## Project usage

### Makefile

The included `Makefile` provides shortcuts for common dev tasks:

- **install**: Set up the virtual environment, install project and development dependencies.
- **setup**: Run `install` and install pre-commit hooks. 
- **run**: Run the main app
- **lint**: Run linting checks with ruff and mypy.
- **format**: Format code with ruff.
- **test**: Run all tests with pytest.
- **clean**: Remove build artifacts, caches, etc.

Example usage:

```bash
make setup    # Set up environment and hooks
make test     # Run tests
make lint     # Lint code
make run      # Run the application
```

### Generating Documentation

Documentation is managed with Sphinx. Initial setup was done with `sphinx-quickstart` and `sphinx-apidoc`.

- Generate API `.rst` files: `make docs-apidoc`
- Build HTML docs: `make docs`
- Remove generated docs under `docs/_build/`: `make docs-clean`

HTML docs will be output to `docs/_build/html`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
