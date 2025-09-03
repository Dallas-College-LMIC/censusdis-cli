# Task Completion Checklist

When completing any development task, always:

## 1. Run Tests
```bash
pytest  # Ensure all tests pass
```

## 2. Code Quality Checks
```bash
ruff format .       # Format code
ruff check --fix .  # Fix linting issues
mypy .             # Type checking
```

## 3. Pre-commit Hooks
```bash
pre-commit run --all-files  # Run all quality checks
```

## 4. Verify Changes
```bash
git status  # Review modified files
git diff    # Review actual changes
```

## 5. Documentation
- Update docstrings if APIs changed
- Update README if user-facing features added
- Add/update tests for new functionality

## Important
- Never skip tests to make things work
- Fix root causes, not symptoms
- Complete all started implementations (no TODOs or placeholders)
