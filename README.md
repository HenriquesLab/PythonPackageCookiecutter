## PythonPackageCookiecutter

A modern Cookiecutter template for Python packages: PEP 621 (`pyproject.toml`), `src/` layout, Ruff, Pytest, and pre-commit ready out of the box.

### Quick start

1) Install Cookiecutter

```bash
pip install cookiecutter
```

2) Generate your new project

```bash
cookiecutter https://github.com/HenriquesLab/PythonPackageCookiecutter
```

3) Follow the prompts, then change into the new folder and set up locally

```bash
cd {{cookiecutter.directory_name}}

# Recommended local setup
pip install -e ".[all]"    # or: .[dev] and .[test]
pre-commit install
pre-commit run --all-files

# Validate everything works
pytest -q
ruff check .
python -m build
```

---

## What you get

- PEP 621 `pyproject.toml` with metadata and optional extras: `dev`, `test`, `all`
- `src/` layout with import-safe packaging configuration
- Ruff linting and formatting (`ruff.toml`)
- Pytest + example test
- Pre-commit configuration and workflow
- Contributor, Code of Conduct, and Changelog starter docs
- Makefile with common development conveniences (optional)

### Generated structure

```
{{cookiecutter.directory_name}}/
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.txt
├── makefile
├── pyproject.toml
├── README.md
├── ruff.toml
├── src/
│   └── {{cookiecutter.package_name}}/
│       ├── __init__.py
│       └── {{cookiecutter.file_name}}.py
└── tests/
	└── test_{{cookiecutter.class_name}}.py
```

Note: the template repository contains a temporary `licenses/` folder that’s removed automatically after generation.

---

## Template prompts (variables)

When you run Cookiecutter, you’ll be asked for:

- `author_name`: Your name for package metadata
- `author_email`: Your email for metadata/contact
- `directory_name`: Top-level project directory/repo name
- `file_name`: Initial module file name inside your package
- `package_name`: Import/distribution name (PEP 8, no underscores enforced)
- `class_name`: Class name used in the example test
- `description`: Short project description
- `minimum_python_version`: Minimum Python (e.g., `3.9`) used for classifiers and `requires-python`
- `license`: Choose from common licenses; `LICENSE.txt` will be created accordingly

Validation: the template enforces PEP 8–style package names and discourages underscores in `package_name`.

---

## Next steps after generation

```bash
cd {{cookiecutter.directory_name}}

# Install with all dev/test extras
pip install -e ".[all]"

# Optional: set up git now
git init
git add .
git commit -m "chore: bootstrap project from cookiecutter"

# Install and run pre-commit hooks
pre-commit install
pre-commit run --all-files

# Run tests / lint / build
pytest -q
ruff check .
ruff format .
python -m build
```

---

## Why `src/` layout?

The `src/` layout prevents accidental imports from the working directory and matches modern packaging guidance. It ensures your tests import the installed package, not local files.

---

## Troubleshooting

- “cookiecutter: command not found”: install with `pip install cookiecutter` (or `pipx install cookiecutter`).
- Windows PowerShell users: use double quotes around extras: `pip install -e ".[all]"`.
- If `ruff` or `pytest` aren’t found, ensure you installed dev/test extras (`.[all]`, or `.[dev]` and `.[test]`).

---

## License

This repository is the template. Projects you generate can use any of the offered licenses; a matching `LICENSE.txt` will be included in the generated project.