# Testing Strategy

## Test-Driven Development (TDD)
Follow the Red-Green-Refactor cycle:
- **Red**: Write failing test first
- **Green**: Write minimal code to pass
- **Refactor**: Improve code while keeping tests green

## Test Guidelines
- **Test Location**: Place tests in `tests/` directory
- **Test Naming**: Use `test_*.py` for test files
- **TDD Guard**: Use `uv run pytest --tdd` for automatic test re-runs during development
- **Mocking**: Use pytest-mock to mock censusdis functions

## Testing Focus
- Mock censusdis functions - don't test the library itself
- Test JSON output format consistency
- Test error handling and structured error responses
- Aim for 100% coverage of CLI wrapper code
