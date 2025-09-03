# AGENTS.md

Project-specific instructions for censusdis-cli - A command-line interface for the censusdis Python library.

## Project Overview

This is a Python CLI tool built on top of the `censusdis` library (>=1.4.2) for accessing and analyzing US Census data. The project uses modern Python tooling with uv for dependency management, pytest for testing, and comprehensive pre-commit hooks for code quality.

## Development Commands

### Running Tests
```bash
# Run all tests
pytest

# Run tests with TDD guard (auto-reruns on file changes)
pytest --tdd

# Run specific test file
pytest tests/test_module.py

# Run with coverage
pytest --cov
```

### Code Quality
```bash
# Format code with ruff
ruff format .

# Lint code with ruff
ruff check --fix .

# Type check with mypy
mypy .

# Run all pre-commit hooks
pre-commit run --all-files
```

### Dependency Management
```bash
# Add a runtime dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Install all dependencies
uv sync

# Update dependencies
uv lock --upgrade
```

## Testing Strategy

- **Test-Driven Development (TDD)**: Follow Red-Green-Refactor cycle
  - Write failing test first (Red)
  - Write minimal code to pass (Green)
  - Refactor while keeping tests green
- **Test Location**: Place tests in `tests/` directory (create if needed)
- **Test Naming**: Use `test_*.py` for test files
- **TDD Guard**: Use `pytest --tdd` for automatic test re-runs during development

## Code Quality Tools

### Pre-commit Hooks (Auto-configured)
- **Python**: ruff (linting & formatting), mypy (type checking)
- **File Hygiene**: trailing whitespace, end-of-file fixer, merge conflict check
- **Format Validation**: YAML, JSON, TOML, Python AST checking
- **Nix**: nixfmt, deadnix, statix, flake-checker

### Python Standards
- Python 3.13+ required
- Type hints encouraged for public APIs
- Follow PEP 8 (enforced by ruff)
- Maximum line length: 88 characters (Black/ruff default)

## Project Structure

```
censusdis-cli/
├── main.py              # Entry point (currently placeholder)
├── pyproject.toml       # Project metadata and dependencies
├── flake.nix           # Nix development environment
├── tests/              # Test directory (create as needed)
├── .ruler/             # AI agent instructions
├── .venv/              # Virtual environment (auto-managed by uv)
└── uv.lock             # Locked dependencies
```

## Development Workflow

1. **Environment Setup**: Project uses Nix flakes with direnv for automatic environment activation
2. **Virtual Environment**: Managed automatically by uv, no manual activation needed
3. **Pre-commit Hooks**: Automatically run on git commit to ensure code quality
4. **Dependencies**: All Python dependencies managed through `pyproject.toml` and `uv.lock`

## Important Implementation Notes

- The `censusdis` library is the core dependency for Census data operations
- Current `main.py` is a placeholder - implement CLI functionality here
- Consider using a CLI framework like `click` or `typer` for command parsing
- Follow existing project patterns - check neighboring files before adding new dependencies

## Architecture Considerations

When implementing the CLI:
1. Separate concerns: CLI interface, data fetching, data processing, output formatting
2. Make operations testable by avoiding direct I/O in business logic
3. Use dependency injection for external services (Census API client)
4. Implement proper error handling with user-friendly messages
5. Consider supporting multiple output formats (JSON, CSV, tables)
