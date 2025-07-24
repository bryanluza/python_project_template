# Cookiecutter Python

## Description (# TODO: Merge whatever is relevant from purpose and context into a project description, don't want to include personal stuff.)
A new Python project template for quick starts.

### Context
I'm learning how to code in Python and I'm aiming to incorporate best practices and conventions as I learn. I'm currently developing a personal Python project template and my goal is to convert this into a GitHub template for efficient project initiation.

### Purpose
I'm creating this file to document the project structure and the tools I'll be using to manage it and develop. I will also be using this document as a contextual foundation for AI chat prompts, to ensure consistent and informed discussions related to this project. For the most part I'm pretty new to most of the tools and standarts I'm planning to use here. I'm pretty open to suggestions and ideas for any improvement I could make to my project.

## Features (# TODO: Add content to this section or remove it. Would Key Technologies & Tools be a subsection of Features?)

## Key Technologies & Tools:

### Development Dependencies (# TODO: Is uv a dev dependency to mention here? I want to mention it but it's not part of the actual project's dev dependencies. Same for git and GitHub?)
- uv: project/package management, using pyproject.toml and uv.lock
- ruff: code formatting and linting
- pre-commit: git hooks manager using pre-commit-config.yaml
- pytest: unit testing
- mypy: static type checker
- sphinx: documentation generation

### Project Dependencies (# TODO: expand a little more on the descriptions.)
- pydantic: Type hinting and documentation
- pydantic-settings for reading .env file

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

## Setup (# TODO: Create detailed instructions on how to get the project setup from using the GitHub template to the uv setup)
1. Install uv on development PC. uv will manage the rest of the projects and dev requirements.
2. Use template to start repository.
3. Update template's placeholders.
4. Set up the virtual environment, install all the pre-defined dependencies and Pre-Commit Hooks: `make install`

## Using This Template

To start a new project using this template:

```bash
pipx install cookiecutter
cookiecutter gh:bryanluza/python_project_template
```

You’ll be prompted for project name, author, etc. All placeholders will be automatically replaced.

### Makefile (# TODO: Add details to this section. Maybe just a short explanation to each command.)
Included Makefile is very simple but a great place to group commonly used commands (and not having to remember them) and probably helpful as projects grow. These are the commands currently included:
- install
- setup
- run
- lint
- format
- test
- clean

### Documentation (# TODO: Review if more details are needed.)
**Note:** Initial setup already done using `sphinx-quickstart` and `sphinx-apidoc`.
- Automatically generate the .rst structure: `make docs-apidoc`
- Generate docs in html: `make docs`
- Clean generated documentation: `make docs-clean`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
