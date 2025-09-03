# Development Commands

## Running Python Scripts
```bash
# Run the main entry point
uv run main.py

# Run any Python script
uv run path/to/script.py

# Run Python modules
uv run -m module_name
```

## Running Tests
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

## Code Quality
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

## Dependency Management
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

## Development Workflow
1. **Environment Setup**: Project uses Nix flakes with direnv for automatic environment activation
2. **Virtual Environment**: Managed automatically by uv, no manual activation needed
3. **Pre-commit Hooks**: Automatically run on git commit to ensure code quality
4. **Dependencies**: All Python dependencies managed through `pyproject.toml` and `uv.lock`
