"""Tests for the CLI wrapper."""

from click.testing import CliRunner
from unittest.mock import patch
import subprocess
import sys
import json
import pandas as pd


def test_cli_exists():
    """Test that the CLI module and command group exist."""
    from src.cli import cli

    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert "Census data discovery CLI" in result.output


def test_main_entry_point():
    """Test that main.py entry point works."""
    result = subprocess.run(
        [sys.executable, "main.py", "--help"], capture_output=True, text=True
    )

    assert result.returncode == 0
    assert "Census data discovery CLI" in result.stdout


def test_datasets_command():
    """Test that datasets command calls censusdis and returns JSON."""
    from src.cli import cli

    # Create a mock DataFrame to return
    mock_df = pd.DataFrame(
        [
            {
                "DATASET": "acs/acs5",
                "TITLE": "American Community Survey 5-Year Data",
                "YEAR": 2020,
            },
            {
                "DATASET": "dec/pl",
                "TITLE": "Decennial Census P.L. 94-171 Redistricting Data",
                "YEAR": 2020,
            },
        ]
    )

    with patch("censusdis.data.variables.all_data_sets", return_value=mock_df):
        runner = CliRunner()
        result = runner.invoke(cli, ["datasets"])

        assert result.exit_code == 0
        output = json.loads(result.output)
        assert len(output) == 2
        assert output[0]["DATASET"] == "acs/acs5"
        assert output[1]["DATASET"] == "dec/pl"


def test_datasets_command_with_year():
    """Test that datasets command filters by year when provided."""
    from src.cli import cli

    mock_df = pd.DataFrame(
        [
            {
                "DATASET": "acs/acs5",
                "TITLE": "American Community Survey 5-Year Data",
                "YEAR": 2021,
            }
        ]
    )

    with patch(
        "censusdis.data.variables.all_data_sets", return_value=mock_df
    ) as mock_func:
        runner = CliRunner()
        result = runner.invoke(cli, ["datasets", "--year", "2021"])

        assert result.exit_code == 0
        mock_func.assert_called_once_with(year=2021)
        output = json.loads(result.output)
        assert len(output) == 1
        assert output[0]["YEAR"] == 2021


def test_search_datasets_command():
    """Test that search-datasets command calls censusdis and returns JSON."""
    from src.cli import cli

    mock_df = pd.DataFrame(
        [{"DATASET": "acs/acs5", "TITLE": "American Community Survey 5-Year Data"}]
    )

    with patch(
        "censusdis.data.variables.search_data_sets", return_value=mock_df
    ) as mock_func:
        runner = CliRunner()
        result = runner.invoke(cli, ["search-datasets", "acs"])

        assert result.exit_code == 0
        mock_func.assert_called_once_with("acs")
        output = json.loads(result.output)
        assert len(output) == 1
        assert output[0]["DATASET"] == "acs/acs5"


def test_groups_command():
    """Test that groups command calls censusdis and returns JSON."""
    from src.cli import cli

    mock_df = pd.DataFrame([{"GROUP": "B01001", "DESCRIPTION": "Sex by Age"}])

    with patch(
        "censusdis.data.variables.search_groups", return_value=mock_df
    ) as mock_func:
        runner = CliRunner()
        result = runner.invoke(cli, ["groups", "acs/acs5", "2020"])

        assert result.exit_code == 0
        mock_func.assert_called_once_with("acs/acs5", 2020, pattern=None)
        output = json.loads(result.output)
        assert len(output) == 1
        assert output[0]["GROUP"] == "B01001"


def test_variables_command():
    """Test that variables command calls censusdis and returns JSON."""
    from src.cli import cli

    mock_df = pd.DataFrame([{"NAME": "B01001_001E", "LABEL": "Total Population"}])

    with patch("censusdis.data.variables.search", return_value=mock_df) as mock_func:
        runner = CliRunner()
        result = runner.invoke(cli, ["variables", "acs/acs5", "2020"])

        assert result.exit_code == 0
        mock_func.assert_called_once_with("acs/acs5", 2020, pattern=None, group=None)
        output = json.loads(result.output)
        assert len(output) == 1
        assert output[0]["NAME"] == "B01001_001E"


def test_geography_command():
    """Test that geography command calls censusdis and returns JSON."""
    from src.cli import cli

    # Mock the geo_path_snake_specs to return a list
    mock_result = ["state", "county", "tract"]

    with patch(
        "censusdis.geography.geo_path_snake_specs", return_value=mock_result
    ) as mock_func:
        runner = CliRunner()
        result = runner.invoke(cli, ["geography", "acs/acs5", "2020"])

        assert result.exit_code == 0
        mock_func.assert_called_once_with("acs/acs5", 2020)
        output = json.loads(result.output)
        assert len(output) == 3
        assert "state" in output


def test_tree_command():
    """Test that tree command calls censusdis and returns JSON."""
    from src.cli import cli

    # Mock the group_tree to return a hierarchical structure
    mock_result = {
        "B01001": {"label": "Sex by Age", "variables": ["B01001_001E", "B01001_002E"]}
    }

    with patch(
        "censusdis.data.variables.group_tree", return_value=mock_result
    ) as mock_func:
        runner = CliRunner()
        result = runner.invoke(cli, ["tree", "acs/acs5", "2020", "B01001"])

        assert result.exit_code == 0
        mock_func.assert_called_once_with("acs/acs5", 2020, "B01001")
        output = json.loads(result.output)
        assert "B01001" in output
