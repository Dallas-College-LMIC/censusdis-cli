# Project Overview

**censusdis-cli** is a thin CLI wrapper around the censusdis library's existing discovery functions, providing an agent-friendly JSON interface for Census data exploration.

## Core Principle
We're not reimplementing discovery - censusdis already has all the functionality. Our CLI simply wraps their functions with JSON output for AI agents.

## Technology Stack
- **Language**: Python 3.13+
- **CLI Framework**: Click
- **Census Library**: censusdis >= 1.4.2 (provides all discovery logic)
- **Testing**: pytest with TDD approach
- **Dependencies**: uv for package management
- **Quality Tools**: ruff, mypy, pre-commit hooks

## Project Structure
```
censusdis-cli/
├── censusdis_cli/       # Package directory
│   ├── __init__.py     # Package initialization
│   └── cli.py          # CLI implementation
├── tests/               # Test directory
├── pyproject.toml       # Project metadata, dependencies, and CLI entry point
├── flake.nix           # Nix development environment
├── .ruler/             # AI agent instructions
├── .venv/              # Virtual environment (auto-managed by uv)
└── uv.lock             # Locked dependencies
```

## Installation
- **Development**: `uv sync` or `uv pip install -e .`
- **Production**: `uv pip install .`
- **CLI Command**: After installation, run `census-discover`

## Key Features
- Dataset discovery and search
- Variable and group exploration
- Geographic level listing
- Hierarchical variable navigation
- JSON output for all commands
- Structured error handling
