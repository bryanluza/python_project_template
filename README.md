# Cookiecutter Python

TODO: Merge whatever is relevant from purpose and context into a project description, ommit personal stuff.

## Description
A new Python project template for quick starts.

### Context
I'm learning how to code in Python and I'm aiming to incorporate best practices and conventions as I learn. I'm currently developing a personal Python project template and my goal is to convert this into a GitHub template for efficient project initiation.

### Purpose
I'm creating this file to document the project structure and the tools I'll be using to manage it and develop. I will also be using this document as a contextual foundation for AI chat prompts, to ensure consistent and informed discussions related to this project. For the most part I'm pretty new to most of the tools and standarts I'm planning to use here. I'm pretty open to suggestions and ideas for any improvement I could make to my project.

## Features

- TODO

## Project structure and files
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

To start a new project using this template:

```bash
pipx install cookiecutter
cookiecutter gh:bryanluza/python_project_template
```

You’ll be prompted for project name, author, etc. All placeholders will be automatically replaced.

**Placeholder locations:**
- pyproject.toml
- LICENSE
- app/main.py
- tests/test_main.py
- docs/config.py

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
