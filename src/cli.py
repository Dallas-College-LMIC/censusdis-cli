"""CLI commands wrapping censusdis discovery functions."""

import click
import json
import censusdis.data as ced  # type: ignore[import-untyped]
import censusdis.geography as cgeo  # type: ignore[import-untyped]


@click.group()
def cli() -> None:
    """Census data discovery CLI for AI agents."""
    pass


@cli.command()
@click.option("--year", type=int, help="Filter by year")
def datasets(year):
    """List all available Census datasets."""
    try:
        df = ced.variables.all_data_sets(year=year)
        result = df.to_dict("records")
        click.echo(json.dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "datasets"}
        click.echo(json.dumps(error), err=True)
        raise SystemExit(1)


@cli.command("search-datasets")
@click.argument("pattern")
def search_datasets(pattern):
    """Search for datasets by pattern."""
    try:
        df = ced.variables.search_data_sets(pattern)
        result = df.to_dict("records")
        click.echo(json.dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "search-datasets"}
        click.echo(json.dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
@click.option("--pattern", help="Search pattern")
def groups(dataset, year, pattern):
    """Search for variable groups in a dataset."""
    try:
        df = ced.variables.search_groups(dataset, year, pattern=pattern)
        result = df.to_dict("records")
        click.echo(json.dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "groups"}
        click.echo(json.dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
@click.option("--pattern", help="Search pattern")
@click.option("--group", help="Variable group")
def variables(dataset, year, pattern, group):
    """Search for variables in a dataset."""
    try:
        df = ced.variables.search(dataset, year, pattern=pattern, group=group)
        result = df.to_dict("records")
        click.echo(json.dumps(result, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "variables"}
        click.echo(json.dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
def geography(dataset, year):
    """List geographic levels for a dataset."""
    try:
        result = cgeo.geo_path_snake_specs(dataset, year)
        # Convert the result to a serializable format
        if hasattr(result, "to_dict"):
            output = result.to_dict("records")
        else:
            # It might be a list or other structure
            output = result
        click.echo(json.dumps(output, indent=2))
    except Exception as e:
        error = {"error": str(e), "command": "geography"}
        click.echo(json.dumps(error), err=True)
        raise SystemExit(1)


@cli.command()
@click.argument("dataset")
@click.argument("year", type=int)
@click.argument("group")
def tree(dataset, year, group):
    """Show variable hierarchy for a group."""
    try:
        result = ced.variables.group_tree(dataset, year, group)
        # The tree might return a different structure
        if hasattr(result, "to_dict"):
            output = result.to_dict("records")
        else:
            output = result
        click.echo(json.dumps(output, indent=2, default=str))
    except Exception as e:
        error = {"error": str(e), "command": "tree"}
        click.echo(json.dumps(error), err=True)
        raise SystemExit(1)
