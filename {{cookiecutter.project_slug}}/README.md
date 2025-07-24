# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Features

- TODO

## Development Dependencies (# TODO: Is uv a dev dependency to mention here? I want to mention it but it's not part of the actual project's dev dependencies. Same for git and GitHub?)
- uv: project/package management, using pyproject.toml and uv.lock
- ruff: code formatting and linting
- pre-commit: git hooks manager using pre-commit-config.yaml
- pytest: unit testing
- mypy: static type checker
- sphinx: documentation generation

## Project Dependencies (# TODO: expand a little more on the descriptions.)
- pydantic: Type hinting and documentation
- pydantic-settings for reading .env file


## Usage

### Makefile (# TODO: Add details to this section. Maybe just a short explanation to each command.)
*Install uv on development PC if not already installed:*
```bash
   pipx install uv
```

Included Makefile is very simple but a great place to group commonly used commands (and not having to remember them) and probably helpful as projects grow. These are the commands currently included:
- Set up the virtual environment, install all the pre-defined dependencies and Pre-Commit Hooks: `make install`
- setup
- run
- lint
- format
- test
- clean

### Generate Documentation (# TODO: Review if more details are needed.)
**Note:** Initial setup already done using `sphinx-quickstart` and `sphinx-apidoc`.
- Automatically generate the .rst structure: `make docs-apidoc`
- Generate docs in html: `make docs`
- Clean generated documentation: `make docs-clean`

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
