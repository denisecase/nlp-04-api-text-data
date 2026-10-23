# nlp-04-api-text-data

[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![CI](https://github.com/denisecase/nlp-04-api-text-data/actions/workflows/ci-python-zensical.yml/badge.svg)](https://github.com/denisecase/nlp-04-api-text-data/actions/workflows/ci-python-zensical.yml)
[![Documentation](https://img.shields.io/badge/docs-site-blue?logo=github)](https://denisecase.github.io/nlp-04-api-text-data/)

[![uv managed](https://img.shields.io/badge/uv-managed-DE5FE9)](https://docs.astral.sh/uv/)
[![ty type checked](https://img.shields.io/badge/ty-type_checked-2F80ED)](https://docs.astral.sh/ty/)
[![Zensical docs](https://img.shields.io/badge/Zensical-docs-purple)](https://zensical.org/)
[![MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> Acquire, validate, and transform JSON data from web APIs using Python.

## Project Overview

Author: Denise Case

Date: 2026 October

Fourth project in the Web Mining and Applied NLP course.

This project introduces structured data acquisition
using web APIs.

The goal is to retrieve JSON data,
validate its structure,
transform it into an analysis-ready dataset,
and persist the results.

The project demonstrates an Extract, Validate,
Transform, Load (EVTL) pipeline.

The project is configured in
[pyproject.toml](pyproject.toml).

## Data

The example retrieves JSON records from
[JSONPlaceholder](https://jsonplaceholder.typicode.com/posts),
a public demonstration API.

Each record includes fields such as:

- User identifier.
- Post identifier.
- Title.
- Body text.

The pipeline preserves the raw JSON data
and produces a structured CSV dataset.

## Approach

The project uses a modular Python pipeline
to acquire, validate, transform, and save API data.

The pipeline has four stages:

- **Extract** - retrieve JSON data from an API.
- **Validate** - verify the JSON structure and record types.
- **Transform** - select fields and calculate derived text features.
- **Load** - save the processed data to a CSV file.

The example uses Requests for HTTP acquisition
and Polars for tabular data processing.

Explore these important project components:

- [pyproject.toml](pyproject.toml) - project identity, dependencies, and tool configuration.
- [src/nlp/pipeline_api_json.py](src/nlp/pipeline_api_json.py) - main EVTL pipeline orchestrator.
- [src/nlp/config.py](src/nlp/config.py) - example API and path configuration.
- [src/nlp/stage01_extract.py](src/nlp/stage01_extract.py) - retrieve API data.
- [src/nlp/stage02_validate.py](src/nlp/stage02_validate.py) - validate JSON data.
- [src/nlp/stage03_transform.py](src/nlp/stage03_transform.py) - transform records into a DataFrame.
- [src/nlp/stage04_load.py](src/nlp/stage04_load.py) - save processed results.
- [tests/](tests/) - automated tests.
- [.github/workflows/](.github/workflows/) - automated testing and documentation deployment.
- [docs/](docs/) - project documentation.
- [zensical.toml](zensical.toml) - documentation configuration.

The goal is to understand how data moves
through a reproducible pipeline
with explicit stages and intermediate results.

## Run the Project

Follow the [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
to set up your machine and project environment.

From a VS Code terminal in the project root:

```shell
uv run python -m nlp.pipeline_api_json
```

## Results

The pipeline retrieves JSON records,
checks their structure,
and transforms the records into a tabular dataset.

The Transform stage calculates derived fields,
including title and body text lengths.

Successful execution produces:

```shell
========================
Pipeline executed successfully!
========================
```

The following files are created:

- `project.log` - pipeline execution log.
- `data/raw/case_raw.json` - original API response.
- `data/processed/case_processed.csv` - transformed dataset.

These artifacts provide evidence of successful
data acquisition, validation, transformation, and persistence.

## Verification

Run the automated tests:

```shell
uv run python -m pytest
```

## Project Documentation

The [hosted documentation site](https://denisecase.github.io/nlp-04-api-text-data/)
is published using Zensical and GitHub Pages.

The documentation site is used to present the project report,
covering such sections as data, methods, results, visualizations,
interpretation, and conclusions.

## CI/CD and GitHub Actions

This project includes continuous integration and continuous deployment (CI/CD)
to check project files and publish the docs.

GitHub Actions include:

- [CI: Python and Documentation Checks](https://github.com/denisecase/nlp-04-api-text-data/actions/workflows/ci-python-zensical.yml)
- [CD: Documentation Deployment](https://github.com/denisecase/nlp-04-api-text-data/actions/workflows/deploy-zensical.yml)

## Developer Reference

Follow the
[Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
for **detailed instructions and troubleshooting**.

### Initialize and Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uvx prek install --force
uvx prek update --freeze --cooldown-days 7

git add -A
uvx prek run --all-files
# repeat if changes were made
uvx prek run --all-files
```

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Developer Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.

## Developer Tools

This project uses professional Python tools to support development,
testing, documentation, and code quality.

- [uv](https://docs.astral.sh/uv/) - Python environments and dependencies.
- [Ruff](https://docs.astral.sh/ruff/) - Python linting and formatting, configured in [.ruff.toml](.ruff.toml).
- [ty](https://docs.astral.sh/ty/) - Python type checking.
- [pytest](https://docs.pytest.org/) - automated Python testing, configured in [.pytest.toml](.pytest.toml).
- [prek](https://prek.j178.dev/) - Git hooks and automated checks, configured in [prek.toml](prek.toml).
- [Zensical](https://zensical.org/) - project documentation, configured in [zensical.toml](zensical.toml).

## Links

- [Hosted Documentation](https://denisecase.github.io/nlp-04-api-text-data/)
- [Professional Python Workflow Guide](https://denisecase.github.io/pro-analytics-02/)
- [Citation](CITATION.cff)
- [License](LICENSE)
