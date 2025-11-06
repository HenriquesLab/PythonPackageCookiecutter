# Contributing to {{cookiecutter.package_name}}

Welcome! We're excited that you're interested in contributing to {{cookiecutter.package_name}}. This guide explains how to report issues, propose features, improve docs, and contribute code in a consistent, low-friction way.

## 🎯 Local-first workflow

We favor fast, local feedback before CI:
- Catch issues quickly with pre-commit, linting, and tests
- Keep CI lean; push only when local checks pass
- Minimize external dependencies and network access

## 🌟 Ways to contribute

### 🐛 Bug reports
- Search existing issues to avoid duplicates
- Include steps to reproduce, expected vs. actual behavior
- Add environment info, logs, and a minimal example when possible

### 💡 Feature requests
- Explain the use case and why it helps
- Keep scope focused and well-defined
- Start a discussion for larger proposals

### 📖 Documentation
- Fix typos, improve clarity, add examples
- Update README, API docs, tutorials, FAQs

### 🔧 Code contributions
- Small, focused PRs are best
- Add tests for new or changed behavior
- Keep changes backward compatible when possible

## 🚀 Getting started

### 1) Fork and clone
```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR_USERNAME/{{cookiecutter.directory_name}}.git
cd {{cookiecutter.directory_name}}
git remote add upstream https://github.com/OWNER/{{cookiecutter.directory_name}}.git
```

### 2) Set up the development environment
```bash
# Install in editable mode with dev extras
pip install -e ".[dev]"

# Install git hooks
pre-commit install

# Run once to verify setup
pre-commit run --all-files
```

### 3) Branch and commit
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-number-description
```

## 🧪 How to test and validate

The project uses tools configured in `pyproject.toml`.

```bash
# Run tests
pytest -q

# Lint
ruff check .

# Format (apply formatting fixes)
ruff format .

# Build the package (sanity check build)
python -m build
```

Tip: run `pre-commit run --all-files` to execute the full suite of local checks before pushing.

## 📝 Pull request checklist

Before opening a PR, please ensure:
- [ ] Tests pass locally (`pytest`)
- [ ] Lint is clean (`ruff check .`) and code is formatted (`ruff format .`)
- [ ] Package builds (`python -m build`)
- [ ] Docs updated if needed
- [ ] `CHANGELOG.md` updated for notable changes

### PR process
1. Use conventional commit style in the title (feat:, fix:, docs:, refactor:, etc.)
2. Describe the change and link related issues
3. Explain how you tested it
4. Call out any breaking changes

## 🎯 Coding standards

### Python style
We use modern tooling for consistent quality:

```bash
pre-commit run --all-files
```

Tools:
- Ruff for linting/formatting (replaces flake8, isort, Black)
- Pytest for testing

Guidelines:
- Use type hints in public APIs
- Include Google-style docstrings for public functions
- Prefer clear names and small, focused functions
- Handle errors with meaningful exceptions and messages

## 🧪 Test structure (suggested)

```
tests/
├── unit/
├── integration/
├── fixtures/
└── conftest.py
```

## 📚 Documentation

Types:
1. Code comments and docstrings
2. API reference (can be generated via docstrings)
3. How-to guides and examples
4. Troubleshooting/FAQ

Writing tips:
- Be concise and example-driven
- Keep structure consistent
- Prefer relative links for internal docs

## 🏷️ Labels (examples)

- `bug`, `enhancement`, `documentation`, `good first issue`, `help wanted`, `question`
- `breaking change`, `feature`, `bugfix`, `docs`, `refactor`, `tests`

## 🚀 Release process (overview)

We follow [Semantic Versioning](https://semver.org/):
- MAJOR: breaking changes
- MINOR: new features
- PATCH: bug fixes

Typical steps:
1. Update `CHANGELOG.md`
2. Bump version
3. Create a GitHub release with notes
4. Publish to PyPI (manually or via CI)

## 📜 Code of Conduct

This project follows our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

## ❓ Getting help

- Open a GitHub issue for bugs and feature requests
- Use Discussions for questions
- For sensitive matters, contact the maintainers at {{cookiecutter.author_email}}

Thanks for contributing to {{cookiecutter.package_name}}! Your help makes the project better for everyone. 🚀