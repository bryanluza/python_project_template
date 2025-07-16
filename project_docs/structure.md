# Python Project Template
## Context
I'm learning how to code in Python and I'm aiming to incorporate best practices and conventions as I learn. I'm currently developing a personal Python project template and my goal is to convert this into a GitHub template for efficient project initiation.

## Purpose
I'm creating this file to document the project structure and the tools I'll be using to manage it and develop. I will also be using this document as a contextual foundation for AI chat prompts, to ensure consistent and informed discussions related to this project. For the most part I'm pretty new to most of the tools and standarts I'm planning to use here. I'm pretty open to suggestions and ideas for any improvement I could make to my project.

## Key Technologies & Tools:

### Development Dependencies
- ruff: code formatting and linting *
- pre-commit: git hooks manager using pre-commit-config.yaml *
- pytest: unit testing *
- mypy: static type checker *
- Open to other suggestions

### Project Dependencies
- pydantic: Type hinting *
- pydantic-settings for reading .env file *
- Open to other suggestions.

### Other
- uv: project/package management, using pyproject.toml and uv.lock
- git for version control
- github for online hosting this template and future projects
-

## Best practices to follow
- Naming Conventions (PEP 8)
- Docstrings (PEP 257)
- Type Hinting (PEP 484) *
- Specific error handling *
- Logging (instead of printing) *

(*) Concepts new to me or that I have very little experience with

## Future plans/ideas
- Add .github directory and implement GitHub CI workflows

## Project structure and files
```
my_project/
├── .git/                   # Git repository metadata (managed by git)
├── .github/                # GitHub specific files (workflows, issue templates)
│   └── workflows/
│       └── ci.yml          # CI workflow setup
├── .venv/                  # Virtual environment (managed by uv)
├── app/                    # Main package directory
│   ├── __init__.py
│   └── main.py
├── docs/                   # Sphinx documentation
├── tests/                  # Unit and integration tests
│   ├── __init__.py
│   └── test_main.py
├── .gitignore              # Files/directories to ignore in Git
├── .pre-commit-config.yaml # Pre-commit hooks configuration
├── .python-version         # Python version (created by uv)
├── CHANGELOG.md            # Project changelog
├── LICENSE                 # Project license (MIT in your case)
├── makefile                 # Automate common development tasks
├── pyproject.toml          # Project metadata, dependencies, and tool configurations
├── README.md               # Project description, installation, usage
└── uv.lock                 # Managed by uv
```
