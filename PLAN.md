# Census Discovery CLI - Implementation Plan

## Project Specification

### Purpose
A thin CLI wrapper around censusdis's existing discovery functions, providing an agent-friendly JSON interface for Census data exploration.

### Core Principle
**We're not reimplementing discovery - censusdis already has it all.** Our CLI simply wraps their functions with JSON output for AI agents.

### Technology Stack
- **Language**: Python 3.13+
- **CLI Framework**: Click
- **Census Library**: censusdis >= 1.4.2 (provides all discovery logic)
- **Testing**: pytest with TDD approach

## censusdis Function Mapping

### What censusdis Already Provides
| censusdis Function | What it Does | Our CLI Command |
|-------------------|--------------|-----------------|
| `ced.variables.all_data_sets(year)` | Lists all available datasets | `datasets` |
| `ced.variables.search_data_sets(pattern)` | Searches dataset names/descriptions | `search-datasets` |
| `ced.variables.search_groups(dataset, year, pattern)` | Searches variable groups | `groups` |
| `ced.variables.search(dataset, year, pattern, group)` | Searches variables | `variables` |
| `cgeo.geo_path_snake_specs(dataset, year)` | Lists geographic levels | `geography` |
| `ced.variables.group_tree(dataset, year, group)` | Shows variable hierarchy | `tree` |

### File Structure (Minimal)
```
censusdis-cli/
├── src/
│   ├── __init__.py
│   └── cli.py          # Single file wrapping censusdis
├── tests/
│   └── test_cli.py     # Tests for the CLI wrapper
└── main.py             # Entry point
```

### CLI Commands
```bash
census-discover datasets [--year YEAR]                    # Wrap all_data_sets()
census-discover search-datasets <pattern>                 # Wrap search_data_sets()
census-discover groups <dataset> <year> [--pattern PAT]   # Wrap search_groups()
census-discover variables <dataset> <year> [--pattern PAT] [--group GRP]  # Wrap search()
census-discover geography <dataset> <year>                # Wrap geo_path_snake_specs()
census-discover tree <dataset> <year> <group>            # Wrap group_tree()
```

## Implementation Phases
Update PLAN.md when finished with each task and make a git commit at the same time.

### Phase 1: Setup
**Goal**: Create minimal structure and install dependencies

#### Tasks
- [x] Create project structure
  - [x] Create `src/` directory and `src/__init__.py`
  - [x] Create `tests/` directory
  - [x] Create `src/cli.py` file
- [x] Install dependencies
  - [x] Add click: `uv add click`
  - [x] Add pytest-mock: `uv add --dev pytest-mock`
- [x] Setup entry point
  - [x] Wire up `main.py` to call CLI
  - [x] Test basic CLI execution

### Phase 2: Wrap censusdis Discovery Functions
**Goal**: Create CLI commands that directly call censusdis functions

#### Tasks
- [x] Dataset commands
  - [x] Write test for `datasets` command
  - [x] Implement `datasets` → calls `ced.variables.all_data_sets()`
  - [x] Write test for `search-datasets` command
  - [x] Implement `search-datasets` → calls `ced.variables.search_data_sets()`
- [x] Variable commands
  - [x] Write test for `groups` command
  - [x] Implement `groups` → calls `ced.variables.search_groups()`
  - [x] Write test for `variables` command
  - [x] Implement `variables` → calls `ced.variables.search()`
- [x] Structure commands
  - [x] Write test for `geography` command
  - [x] Implement `geography` → calls `cgeo.geo_path_snake_specs()`
  - [x] Write test for `tree` command
  - [x] Implement `tree` → calls `ced.variables.group_tree()`

### Phase 3: JSON Output & Error Handling
**Goal**: Ensure all output is agent-friendly JSON

#### Tasks
- [x] Output formatting
  - [x] Convert pandas DataFrames to JSON
  - [x] Handle NaN and infinity values properly
  - [x] Ensure consistent JSON schema across commands
- [x] Error handling
  - [x] Catch censusdis exceptions
  - [x] Return structured error JSON
  - [x] Test error conditions
- [x] Documentation
  - [x] Add docstrings with examples
  - [ ] Update README with usage
  - [ ] Document JSON output schemas

## Success Criteria

### Core Functionality ✅
- [x] All six censusdis discovery functions wrapped in CLI
- [x] JSON output for all commands
- [x] Structured error messages in JSON
- [x] Tests for each command (11 tests passing)
- [ ] README with examples

## Example Implementation

```python
import click
import json
import censusdis.data as ced
import censusdis.geography as cgeo

@click.group()
def cli():
    """Census data discovery CLI for AI agents."""
    pass

@cli.command()
@click.option('--year', type=int, help='Filter by year')
def datasets(year):
    """List all available Census datasets."""
    try:
        df = ced.variables.all_data_sets(year=year)
        result = df.to_dict('records')
        click.echo(json.dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "datasets"}
        click.echo(json.dumps(error), err=True)

@cli.command()
@click.argument('dataset')
@click.argument('year', type=int)
@click.option('--pattern', help='Search pattern')
def variables(dataset, year, pattern):
    """Search for variables in a dataset."""
    try:
        df = ced.variables.search(dataset, year, pattern=pattern)
        result = df.to_dict('records')
        click.echo(json.dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "variables"}
        click.echo(json.dumps(error), err=True)
```

## Testing Strategy

### TDD with Mocked censusdis
```python
import pytest
from unittest.mock import patch, MagicMock
from click.testing import CliRunner

def test_datasets_command():
    """Test that datasets command calls censusdis and returns JSON."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"dataset": "acs/acs5", "year": 2020}]

    with patch('censusdis.data.variables.all_data_sets', return_value=mock_df):
        runner = CliRunner()
        result = runner.invoke(cli, ['datasets'])
        assert result.exit_code == 0
        assert '"dataset": "acs/acs5"' in result.output
```

## Development Workflow

1. Run tests: `pytest --tdd`
2. Format: `ruff format .`
3. Lint: `ruff check --fix .`

---

*Version*: 0.1.0
*Status*: Ready for Implementation
*Key Insight*: We're just wrapping censusdis - no need to reinvent the wheel!
