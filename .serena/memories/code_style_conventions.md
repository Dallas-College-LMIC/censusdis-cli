# Code Style and Conventions

## Python Standards
- Python 3.13+ required
- Follow PEP 8 (enforced by ruff)
- Maximum line length: 88 characters (Black/ruff default)

## Type Hints
- Use type hints for all public API functions
- Complex variables should have type annotations
- Return types should be explicit

## Naming Conventions
- Functions/variables: snake_case
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE
- Private methods/attributes: prefix with underscore

## Documentation
- Docstrings for all public functions/classes
- Follow Google or NumPy docstring style
- Include parameter types and return values

## Error Handling
- Use specific exception types
- Log errors with context
- User-friendly error messages for CLI

## Testing
- Test files: test_*.py in tests/ directory
- Test functions: test_<functionality>
- Follow TDD: Red-Green-Refactor cycle

## Architecture Principles
- Separate concerns: CLI interface, data fetching, processing, output
- Dependency injection for external services
- Keep functions short and focused
- No direct I/O in business logic (testability)
