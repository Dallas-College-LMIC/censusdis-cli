# Census Discover CLI Reference

A comprehensive guide to using the `census-discover` command-line tool for exploring U.S. Census data. This CLI provides an agent-friendly JSON interface to the powerful [censusdis](https://github.com/censusdis/censusdis) library's discovery functions.

## Table of Contents
- [Overview](#overview)
- [Command Map](#command-map)
- [Discovery Workflow](#discovery-workflow)
- [Command Reference](#command-reference)
- [Practical Examples](#practical-examples)
- [Output Format](#output-format)
- [Common Use Cases](#common-use-cases)

## Overview

The `census-discover` tool is designed as a **thin wrapper** around censusdis library functions, converting their outputs to JSON format for easy consumption by AI agents and automated tools. It doesn't reimlement Census data discovery - it just makes the existing censusdis functionality accessible via command line with structured output.

### Design Philosophy
- **Discovery First**: Help users understand what data is available before downloading
- **Agent-Friendly**: All output in structured JSON format
- **Workflow-Oriented**: Commands designed to follow natural data exploration patterns
- **Error-Safe**: Structured error handling for robust automation

## Command Map

```
census-discover
├── datasets              # Discover available Census datasets
├── search-datasets       # Search datasets by name/description
├── groups               # Find variable groups within a dataset
├── variables            # Search for specific variables
├── geography            # List geographic levels for a dataset
└── tree                 # Show hierarchical structure of variables in a group
```

### Command Relationships
1. **datasets** → Find available data sources
2. **groups** → Explore variable categories within a dataset
3. **variables** → Find specific data points within groups
4. **geography** → Understand geographic granularity options
5. **tree** → Visualize how variables are organized hierarchically

## Discovery Workflow

### Typical Exploration Path
```bash
# 1. Start: What datasets are available?
census-discover datasets --year 2020

# 2. Focus: Search for datasets of interest
census-discover search-datasets "american community"

# 3. Explore: What variable groups exist in this dataset?
census-discover groups acs/acs5 2020 --pattern income

# 4. Detail: What specific variables are in this group?
census-discover variables acs/acs5 2020 --group B19001

# 5. Structure: How are these variables organized?
census-discover tree acs/acs5 2020 B19001

# 6. Geography: What geographic levels are available?
census-discover geography acs/acs5 2020
```

## Command Reference

### `census-discover datasets`

**Purpose**: List all available Census datasets, optionally filtered by year.

**Syntax**:
```bash
census-discover datasets [--year YEAR]
```

**Parameters**:
- `--year`: Optional integer to filter datasets by year (e.g., 2020, 2019)

**Use Cases**:
- Starting point for all data exploration
- Finding datasets for a specific year
- Understanding the full scope of available Census data

**Example Commands**:
```bash
# List all available datasets
census-discover datasets

# List datasets for 2020 only
census-discover datasets --year 2020

# List datasets for 2019
census-discover datasets --year 2019
```

**JSON Output Structure**:
```json
[
  {
    "DATASET": "acs/acs5",
    "TITLE": "American Community Survey: 5-Year Estimates: Detailed Tables 5-Year",
    "YEAR": [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
  },
  {
    "DATASET": "dec/pl",
    "TITLE": "Decennial Census: Redistricting Data (Public Law 94-171) Summary File",
    "YEAR": [2020]
  }
]
```

**Key Fields**:
- `DATASET`: Dataset identifier used in other commands (e.g., "acs/acs5", "dec/pl")
- `TITLE`: Human-readable description of the dataset
- `YEAR`: Array of years when this dataset was available

---

### `census-discover search-datasets`

**Purpose**: Search for datasets by name or description pattern.

**Syntax**:
```bash
census-discover search-datasets PATTERN
```

**Parameters**:
- `PATTERN`: Text pattern to search for in dataset names and descriptions

**Use Cases**:
- Finding datasets related to specific topics (e.g., "community", "economic")
- Locating datasets when you know part of the name
- Discovering related datasets

**Example Commands**:
```bash
# Search for American Community Survey datasets
census-discover search-datasets "community"

# Search for economic datasets
census-discover search-datasets "economic"

# Search for decennial census
census-discover search-datasets "decennial"
```

**JSON Output**: Same structure as `datasets` command, but filtered to matching results.

---

### `census-discover groups`

**Purpose**: Find variable groups within a specific dataset and year.

**Syntax**:
```bash
census-discover groups DATASET YEAR [--pattern PATTERN]
```

**Parameters**:
- `DATASET`: Dataset identifier (e.g., "acs/acs5", "dec/pl")
- `YEAR`: Year as integer (e.g., 2020)
- `--pattern`: Optional search pattern to filter groups

**Use Cases**:
- Exploring what types of data are available in a dataset
- Finding groups related to specific topics
- Understanding the organization of Census variables

**Example Commands**:
```bash
# List all variable groups in ACS 5-year 2020
census-discover groups acs/acs5 2020

# Find income-related groups
census-discover groups acs/acs5 2020 --pattern income

# Find demographic groups
census-discover groups acs/acs5 2020 --pattern race

# Find housing groups
census-discover groups acs/acs5 2020 --pattern housing
```

**JSON Output Structure**:
```json
[
  {
    "GROUP": "B01001",
    "DESCRIPTION": "SEX BY AGE"
  },
  {
    "GROUP": "B19001",
    "DESCRIPTION": "HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN 2020 INFLATION-ADJUSTED DOLLARS)"
  }
]
```

**Key Fields**:
- `GROUP`: Group identifier used in other commands (e.g., "B01001", "B19001")
- `DESCRIPTION`: Human-readable description of what the group contains

**Common Group Patterns**:
- `B01xxx`: Age and sex demographics
- `B19xxx`: Income data
- `B25xxx`: Housing characteristics
- `B08xxx`: Journey to work/commuting
- `C24xxx`: Industry and occupation

---

### `census-discover variables`

**Purpose**: Search for specific variables within a dataset.

**Syntax**:
```bash
census-discover variables DATASET YEAR [--pattern PATTERN] [--group GROUP]
```

**Parameters**:
- `DATASET`: Dataset identifier (e.g., "acs/acs5")
- `YEAR`: Year as integer (e.g., 2020)
- `--pattern`: Optional text pattern to search in variable names/labels
- `--group`: Optional group identifier to limit search (e.g., "B01001")

**Use Cases**:
- Finding specific data points within a dataset
- Exploring variables within a known group
- Searching for variables by topic across all groups

**Example Commands**:
```bash
# List all variables in ACS 5-year 2020 (warning: very large output)
census-discover variables acs/acs5 2020

# Search for income-related variables
census-discover variables acs/acs5 2020 --pattern income

# Get all variables in the B01001 (Sex by Age) group
census-discover variables acs/acs5 2020 --group B01001

# Search for median income specifically
census-discover variables acs/acs5 2020 --pattern "median income"

# Find poverty-related variables
census-discover variables acs/acs5 2020 --pattern poverty
```

**JSON Output Structure**:
```json
[
  {
    "NAME": "B01001_001E",
    "LABEL": "Estimate!!Total",
    "GROUP": "B01001",
    "PREDICATETYPE": "int"
  },
  {
    "NAME": "B01001_002E",
    "LABEL": "Estimate!!Total!!Male",
    "GROUP": "B01001",
    "PREDICATETYPE": "int"
  }
]
```

**Key Fields**:
- `NAME`: Variable identifier for data downloads (e.g., "B01001_001E")
- `LABEL`: Human-readable description of the variable
- `GROUP`: Parent group this variable belongs to
- `PREDICATETYPE`: Data type (usually "int" or "string")

**Variable Naming Patterns**:
- `_E` suffix: Estimates (actual data values)
- `_M` suffix: Margins of error
- `_001`: Usually represents totals
- `_002`, `_003`, etc.: Breakdowns of the total

---

### `census-discover geography`

**Purpose**: List available geographic levels for a dataset and year.

**Syntax**:
```bash
census-discover geography DATASET YEAR
```

**Parameters**:
- `DATASET`: Dataset identifier (e.g., "acs/acs5")
- `YEAR`: Year as integer (e.g., 2020)

**Use Cases**:
- Understanding what geographic granularity is available
- Planning geographic scope for data analysis
- Finding geographic identifiers needed for data downloads

**Example Commands**:
```bash
# See geographic levels for ACS 5-year data
census-discover geography acs/acs5 2020

# Check geographic options for decennial census
census-discover geography dec/pl 2020

# Explore geographic levels for ACS 1-year data
census-discover geography acs/acs1 2022
```

**JSON Output Structure**:
```json
[
  {
    "for": "state:*"
  },
  {
    "for": "county:*",
    "in": "state:*"
  },
  {
    "for": "tract:*",
    "in": "state:* county:*"
  }
]
```

**Key Fields**:
- `for`: The geographic level you're requesting data for
- `in`: Required geographic hierarchy (parent geographies needed)

**Common Geographic Levels**:
- `state`: U.S. states and territories
- `county`: Counties within states
- `tract`: Census tracts within counties
- `block group`: Block groups within tracts
- `congressional district`: Congressional districts
- `metropolitan statistical area/micropolitan statistical area`: Metro areas

---

### `census-discover tree`

**Purpose**: Show the hierarchical structure of variables within a group.

**Syntax**:
```bash
census-discover tree DATASET YEAR GROUP
```

**Parameters**:
- `DATASET`: Dataset identifier (e.g., "acs/acs5")
- `YEAR`: Year as integer (e.g., 2020)
- `GROUP`: Group identifier (e.g., "B01001")

**Use Cases**:
- Understanding how variables in a group are organized
- Finding the relationship between summary and detailed variables
- Visualizing data hierarchy for analysis planning

**Example Commands**:
```bash
# Show structure of Sex by Age variables
census-discover tree acs/acs5 2020 B01001

# Explore income distribution structure
census-discover tree acs/acs5 2020 B19001

# See housing tenure breakdown
census-discover tree acs/acs5 2020 B25003
```

**JSON Output Structure**: (Varies by group, represents hierarchical tree structure)

## Practical Examples

### Example 1: Exploring Income Data

```bash
# 1. Find income-related groups
census-discover groups acs/acs5 2020 --pattern income

# 2. Explore household income distribution group
census-discover variables acs/acs5 2020 --group B19001

# 3. See how income brackets are structured
census-discover tree acs/acs5 2020 B19001

# 4. Check geographic availability
census-discover geography acs/acs5 2020
```

### Example 2: Demographic Analysis Setup

```bash
# 1. Find demographic/population groups
census-discover groups acs/acs5 2020 --pattern "age\|sex\|race"

# 2. Get detailed age and sex breakdown
census-discover variables acs/acs5 2020 --group B01001

# 3. Explore race and ethnicity data
census-discover variables acs/acs5 2020 --group B03002

# 4. Understand variable hierarchies
census-discover tree acs/acs5 2020 B01001
census-discover tree acs/acs5 2020 B03002
```

### Example 3: Housing Market Research

```bash
# 1. Find housing-related groups
census-discover groups acs/acs5 2020 --pattern housing

# 2. Look for specific housing characteristics
census-discover variables acs/acs5 2020 --pattern "tenure\|value\|rent"

# 3. Explore housing value distribution
census-discover tree acs/acs5 2020 B25075

# 4. Check tenure (own vs rent) breakdown
census-discover tree acs/acs5 2020 B25003
```

### Example 4: Starting from Scratch

```bash
# 1. What datasets exist for recent years?
census-discover datasets --year 2020

# 2. What's in the main ACS dataset?
census-discover groups acs/acs5 2020

# 3. What variables are available? (search by topic)
census-discover variables acs/acs5 2020 --pattern education

# 4. How granular can I get geographically?
census-discover geography acs/acs5 2020
```

## Output Format

### Success Response
All successful commands return JSON arrays or objects containing the requested data.

### Error Response
```json
{
  "error": "Error description here",
  "command": "command-name"
}
```

Errors are printed to stderr and the command exits with status code 1.

### Common Error Scenarios
- Invalid dataset identifier
- Year not available for dataset
- Group doesn't exist in dataset/year combination
- Network connectivity issues with Census API

## Common Use Cases

### 1. **Data Discovery for New Projects**
Start with `datasets` → `groups` → `variables` to understand what's available.

### 2. **Finding Specific Data Points**
Use `variables` with `--pattern` to search across all groups for specific topics.

### 3. **Understanding Data Structure**
Use `tree` to see how variables are organized hierarchically within groups.

### 4. **Geographic Planning**
Use `geography` to understand what geographic levels are available for your analysis.

### 5. **Agent-Driven Exploration**
The JSON output format makes it easy for AI agents to programmatically explore Census data structure and build data collection workflows.

## Tips for Effective Use

1. **Start Broad**: Begin with `datasets` and `groups` to get oriented
2. **Use Patterns**: The `--pattern` option is powerful for finding relevant data
3. **Check Geography Early**: Geographic availability varies by dataset
4. **Understand Hierarchies**: Use `tree` to see how detailed variables relate to totals
5. **Combine Commands**: Chain commands together to build complete data discovery workflows

## Next Steps

After discovering the data structure you need:
1. Use the censusdis Python library directly for data downloads
2. Build automated workflows using the JSON output from these commands
3. Create data collection scripts based on the discovered variable names and geographic specifications

This CLI is designed to be the "map" that helps you navigate the vast landscape of U.S. Census data efficiently and systematically.
