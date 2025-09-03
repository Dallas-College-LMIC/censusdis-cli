# CLI Commands

The CLI wraps censusdis functions with JSON output:

| censusdis Function | CLI Command | Purpose |
|-------------------|-------------|----------|
| `ced.variables.all_data_sets(year)` | `census-discover datasets` | List all available datasets |
| `ced.variables.search_data_sets(pattern)` | `census-discover search-datasets` | Search dataset names/descriptions |
| `ced.variables.search_groups(dataset, year, pattern)` | `census-discover groups` | Search variable groups |
| `ced.variables.search(dataset, year, pattern, group)` | `census-discover variables` | Search variables |
| `cgeo.geo_path_snake_specs(dataset, year)` | `census-discover geography` | List geographic levels |
| `ced.variables.group_tree(dataset, year, group)` | `census-discover tree` | Show variable hierarchy |

## Example Usage
```bash
# List all datasets for 2020
census-discover datasets --year 2020

# Search for income-related variables
census-discover variables acs/acs5 2020 --pattern income

# Get geographic levels for a dataset
census-discover geography acs/acs5 2020

# All output will be in JSON format for agent consumption
```

## Implementation Notes
- Each command maps directly to a censusdis function
- All output formatted as JSON for agent consumption
- Structured error handling returns JSON errors
- No reimplementation - just wrapping existing functions
