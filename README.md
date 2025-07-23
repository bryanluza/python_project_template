# {{ PROJECT_NAME }}

## Description (# TODO: remove purpose and context and expand description)
A new Python project template for quick starts.

### Context
I'm learning how to code in Python and I'm aiming to incorporate best practices and conventions as I learn. I'm currently developing a personal Python project template and my goal is to convert this into a GitHub template for efficient project initiation.

### Purpose
I'm creating this file to document the project structure and the tools I'll be using to manage it and develop. I will also be using this document as a contextual foundation for AI chat prompts, to ensure consistent and informed discussions related to this project. For the most part I'm pretty new to most of the tools and standarts I'm planning to use here. I'm pretty open to suggestions and ideas for any improvement I could make to my project.


## Key Technologies & Tools:

### Development Dependencies (# TODO: Is uv a dev dependency (want to mention it but it's not part of the project's dev dependencies)? Same for git and GitHub?)
- uv: project/package management, using pyproject.toml and uv.lock
- ruff: code formatting and linting
- pre-commit: git hooks manager using pre-commit-config.yaml
- pytest: unit testing
- mypy: static type checker
- sphinx: documentation generation

### Project Dependencies (# TODO: expand a little more)
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

## Features (# TODO: Add something or remove section)

## Setup (# TODO: Test, and expand, maybe include uv commands instead or toguether)
1. Clone the Template: Use `git clone --depth 1 <template_repo_url> <new_project_name>`. The `--depth 1` option creates a shallow clone, only getting the latest commit, which is faster and smaller as you don't need the template's history in the new project.
2. Rename and change directory.
3. Remove .git folder: `rm -rf .git` The cloned repository contains the template's .git history, which you don't want. You want a fresh history for the new project.
4. Initialize New Git Repository: `git init`
5. Update placeholder names

6. Set up the virtual environment, install all the pre-defined dependencies and Pre-Commit Hooks: `make install`
7. Initial Commit: Make the first commit for the new project. `git add .` `git commit -m "Initial commit"`

## Usage
### Makefile
- install 
- setup 
- run 
- lint 
- format 
- test 
- clean

### Documentation
**Note:** Initial setup already done using `sphinx-quickstart` and `sphinx-apidoc`. 
- Automatically generate the .rst structure: `make docs-apidoc`
- Generate docs in html: `make docs`
- Clean generated documentation: `make docs-clean`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.