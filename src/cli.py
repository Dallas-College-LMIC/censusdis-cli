"""Census Discovery CLI - Agent-friendly JSON interface for Census data exploration.

This module provides a command-line interface that wraps censusdis library's
discovery functions with JSON output, making Census data exploration accessible
to AI agents and automated tools.

All commands output JSON for easy parsing by agents. Error messages are also
returned as structured JSON with 'error' and 'command' fields.
"""

import click
import json
import math
import pandas as pd
import censusdis.data as ced  # type: ignore[import-untyped]
import censusdis.geography as cgeo  # type: ignore[import-untyped]


def safe_json_dumps(obj, **kwargs):
    """JSON dumps that handles NaN and infinity values by converting them to null."""

    def handle_nan(o):
        if isinstance(o, float):
            if math.isnan(o) or math.isinf(o):
                return None
        return o

    # First pass: clean the object
    if isinstance(obj, list):
        obj = [
            {k: handle_nan(v) for k, v in item.items()}
            if isinstance(item, dict)
            else item
            for item in obj
        ]
    elif isinstance(obj, dict):
        obj = {k: handle_nan(v) for k, v in obj.items()}

    return json.dumps(obj, **kwargs)


def dataframe_to_json(df):
    """Convert a pandas DataFrame to JSON-serializable format."""
    # Just convert to dict, we'll handle NaN in safe_json_dumps
    return df.to_dict("records")


@click.group()
def cli() -> None:
    """Census data discovery CLI for AI agents."""
    pass


@cli.command()
@click.option("--year", type=int, help="Filter by year")
def datasets(year):
    """List all available Census datasets.

    Examples:
        census-discover datasets
        census-discover datasets --year 2020

    Returns JSON array of dataset objects with fields like:
        - DATASET: Dataset identifier (e.g., "acs/acs5")
        - TITLE: Human-readable title
        - YEAR: Available years
    """
    try:
        df = ced.variables.all_data_sets(year=year)
        result = dataframe_to_json(df)
        click.echo(safe_json_dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "datasets"}
        click.echo(safe_json_dumps(error), err=True)
        raise SystemExit(1)


@cli.command("search-datasets")
@click.argument("pattern")
def search_datasets(pattern):
    """Search for datasets by pattern.

    Examples:
        census-discover search-datasets acs
        census-discover search-datasets "community survey"

    Returns JSON array of matching datasets.
    """
    try:
        df = ced.variables.search_data_sets(pattern)
        result = dataframe_to_json(df)
        click.echo(safe_json_dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "search-datasets"}
        click.echo(safe_json_dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
@click.option("--pattern", help="Search pattern")
def groups(dataset, year, pattern):
    """Search for variable groups in a dataset.

    Examples:
        census-discover groups acs/acs5 2020
        census-discover groups acs/acs5 2020 --pattern income

    Returns JSON array of group objects with fields like:
        - GROUP: Group identifier (e.g., "B01001")
        - DESCRIPTION: Human-readable description
    """
    try:
        df = ced.variables.search_groups(dataset, year, pattern=pattern)
        result = dataframe_to_json(df)
        click.echo(safe_json_dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "groups"}
        click.echo(safe_json_dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
@click.option("--pattern", help="Search pattern")
@click.option("--group", help="Variable group")
def variables(dataset, year, pattern, group):
    """Search for variables in a dataset.

    Examples:
        census-discover variables acs/acs5 2020
        census-discover variables acs/acs5 2020 --pattern income
        census-discover variables acs/acs5 2020 --group B01001

    Returns JSON array of variable objects with fields like:
        - NAME: Variable identifier (e.g., "B01001_001E")
        - LABEL: Human-readable label
        - GROUP: Parent group
    """
    try:
        df = ced.variables.search(dataset, year, pattern=pattern, group=group)
        result = dataframe_to_json(df)
        click.echo(safe_json_dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "variables"}
        click.echo(safe_json_dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
def geography(dataset, year):
    """List geographic levels for a dataset.

    Examples:
        census-discover geography acs/acs5 2020
        census-discover geography dec/pl 2020

    Returns JSON array of geographic level specifications.
    """
    try:
        result = cgeo.geo_path_snake_specs(dataset, year)
        # Convert the result to a serializable format
        if hasattr(result, "to_dict"):
            output = dataframe_to_json(result)
        elif isinstance(result, pd.DataFrame):
            output = dataframe_to_json(result)
        else:
            # It might be a list or other structure
            output = result
        click.echo(safe_json_dumps(output, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "geography"}
        click.echo(safe_json_dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
@click.argument("group")
def tree(dataset, year, group):
    """Show variable hierarchy for a group.

    Examples:
        census-discover tree acs/acs5 2020 B01001
        census-discover tree acs/acs5 2020 B19001

    Returns JSON object with hierarchical variable structure.
    """
    try:
        result = ced.variables.group_tree(dataset, year, group)
        # The tree might return a different structure
        if hasattr(result, "to_dict"):
            output = dataframe_to_json(result)
        elif isinstance(result, pd.DataFrame):
            output = dataframe_to_json(result)
        else:
            # Assume it's already a dict/list structure
            output = result
        click.echo(safe_json_dumps(output, indent=2, default=str))
    except Exception as e:
        error = {"error": str(e), "command": "tree"}
        click.echo(safe_json_dumps(error), err=True)
        raise SystemExit(1)
