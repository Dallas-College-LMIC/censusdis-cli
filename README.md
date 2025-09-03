# censusdis-cli

A command-line interface providing agent-friendly JSON output for Census data discovery. This tool wraps the excellent [censusdis](https://github.com/vengroff/censusdis) library's discovery functions, making Census data exploration accessible to AI agents and automated tools.

## Features

- **Dataset Discovery**: Search and explore available Census datasets
- **Variable Exploration**: Find variables and groups within datasets
- **Geographic Levels**: Discover available geographic hierarchies
- **Hierarchical Views**: Explore variable relationships and structures
- **Agent-Friendly**: All output in structured JSON format
- **Error Handling**: Structured error messages for robust automation

## Installation

Since this package is not yet published on PyPI, install directly from GitHub:

### Quick Start with uvx (Recommended)

No installation needed - run directly:

```bash
uvx --from git+https://github.com/yourusername/censusdis-cli.git census-discover --help
```

### Install as a tool with uv

For frequent use, install it as a tool:

```bash
uv tool install git+https://github.com/yourusername/censusdis-cli.git
```

### Development setup

For contributing or modifying the code:

```bash
git clone https://github.com/yourusername/censusdis-cli.git
cd censusdis-cli
uv sync  # Installs all dependencies
uv run census-discover --help
```

## Usage

The CLI provides a `census-discover` command with several subcommands for data discovery.

If you're using uvx (recommended for one-off commands):

### List all datasets

```bash
uvx --from git+https://github.com/yourusername/censusdis-cli.git census-discover datasets
uvx --from git+https://github.com/yourusername/censusdis-cli.git census-discover datasets --year 2020
```

### Search datasets

```bash
uvx --from git+https://github.com/yourusername/censusdis-cli.git census-discover search-datasets acs
uvx --from git+https://github.com/yourusername/censusdis-cli.git census-discover search-datasets "community survey"
```

Or if you've installed it locally or are in the project directory:

### Find variable groups

```bash
# If installed globally
census-discover groups acs/acs5 2020
census-discover groups acs/acs5 2020 --pattern income

# If in project directory
uv run census-discover groups acs/acs5 2020
uv run census-discover groups acs/acs5 2020 --pattern income
```

### Search variables

```bash
census-discover variables acs/acs5 2020
census-discover variables acs/acs5 2020 --pattern income
census-discover variables acs/acs5 2020 --group B01001
```

### Get geographic levels

```bash
census-discover geography acs/acs5 2020
census-discover geography dec/pl 2020
```

### Show variable hierarchy

```bash
census-discover tree acs/acs5 2020 B01001
census-discover tree acs/acs5 2020 B19001
```

## Output Format

All commands output JSON for easy parsing by automated tools and AI agents. Errors are also returned as structured JSON:

```json
{
  "error": "Error message",
  "command": "command-name"
}
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/censusdis-cli.git
cd censusdis-cli

# Install all dependencies including dev tools
uv sync --all-extras
```

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov

# Run with TDD guard (auto-reruns on file changes)
uv run pytest --tdd
```

## Credits

This CLI is a thin wrapper around the [censusdis](https://github.com/vengroff/censusdis) library by Darren Vengroff. All the actual Census data discovery logic is provided by censusdis - we just provide an agent-friendly JSON interface.

## License

[Your license here]
