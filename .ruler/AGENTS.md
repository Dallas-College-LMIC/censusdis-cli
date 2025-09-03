# AGENTS.md

Project-specific instructions for censusdis-cli - A command-line interface for the censusdis Python library.

## Quick Reference

This is a Python CLI tool that wraps the censusdis library's discovery functions with JSON output for agent consumption.

### Key Points
- We're NOT reimplementing discovery - censusdis has it all
- Simple wrapper: each CLI command directly calls a censusdis function
- All output in JSON format for agent-friendly consumption
- Use TDD approach with uv run pytest --tdd
- Mock censusdis in tests, don't test the library itself

### Main Implementation
- Entry point: `census-discover` command (via pyproject.toml scripts)
- CLI logic: `censusdis_cli/cli.py` (single file is sufficient)
- Tests: `tests/` directory
- Framework: Click for CLI parsing
- Installation: `uv sync` or `uv pip install -e .`
