# censusdis-cli Project Overview

## Purpose
A command-line interface tool for discovering and exploring US Census data using the censusdis library. Designed to be used by AI agents to systematically explore available Census datasets, variables, geographies, and metadata to find relevant data points for vague data requests.

## Tech Stack
- Python 3.13+
- censusdis >= 1.4.2 (core Census data library)
- pytest for testing (with TDD guard)
- uv for dependency management
- ruff for linting and formatting
- mypy for type checking
- Nix flakes with direnv for development environment

## Project Structure
- main.py: Entry point (currently placeholder)
- pyproject.toml: Project metadata and dependencies
- tests/: Test directory (to be created)
- .ruler/: AI agent instructions
- .venv/: Virtual environment (auto-managed by uv)

## Development Approach
- Test-Driven Development (TDD) with Red-Green-Refactor cycle
- Type hints for public APIs
- PEP 8 compliance (enforced by ruff)
- Maximum line length: 88 characters
