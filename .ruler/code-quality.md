# Code Quality Standards

## Python Standards
- Python 3.13+ required
- Type hints encouraged for public APIs
- Follow PEP 8 (enforced by ruff)
- Maximum line length: 88 characters (Black/ruff default)

## Pre-commit Hooks (Auto-configured)
- **Python**: ruff (linting & formatting), mypy (type checking)
- **File Hygiene**: trailing whitespace, end-of-file fixer, merge conflict check
- **Format Validation**: YAML, JSON, TOML, Python AST checking
- **Nix**: nixfmt, deadnix, statix, flake-checker

## Quality Tools
- **ruff**: Linting and formatting
- **mypy**: Type checking
- **pytest**: Testing framework
- **pre-commit**: Git hooks for quality checks
