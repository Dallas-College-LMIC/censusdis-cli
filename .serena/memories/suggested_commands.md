# Suggested Commands for censusdis-cli

## Testing Commands
```bash
pytest                      # Run all tests
pytest --tdd               # Run tests with auto-rerun on file changes (TDD guard)
pytest tests/test_file.py  # Run specific test file
pytest --cov              # Run tests with coverage report
```

## Code Quality Commands
```bash
ruff format .             # Format code
ruff check --fix .        # Lint and auto-fix issues
mypy .                    # Type check
pre-commit run --all-files # Run all pre-commit hooks
```

## Dependency Management
```bash
uv add <package>          # Add runtime dependency
uv add --dev <package>    # Add development dependency
uv sync                   # Install all dependencies
uv lock --upgrade         # Update dependencies
```

## Git Commands
```bash
git status               # Check current status
git diff                # View changes
git add .               # Stage changes
git commit -m "message" # Commit changes
```

## Project Execution
```bash
python main.py          # Run the CLI (once implemented)
```
