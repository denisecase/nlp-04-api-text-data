# Project Instructions

## Goal

Apply **API-based data acquisition and transformation**
to retrieve structured text data
and produce an analysis-ready dataset.

Use an Extract, Validate, Transform, Load (EVTL) pipeline.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Retrieves JSON records from a public API.
- Preserves the raw API response.
- Validates the structure of the JSON data.
- Selects fields and creates derived text features.
- Uses Polars to construct a structured dataset.
- Saves the transformed records as a CSV artifact.

Review the purpose of each EVTL stage
and how the data moves between stages.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**nlp-04-api-text-data-custom**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Acquire and prepare text records
from a different JSON API endpoint.

Use the JSONPlaceholder comments endpoint:

https://jsonplaceholder.typicode.com/comments

Keep the original `.py` files as working examples.
Create and modify copies for your custom processing stages.

Update the pipeline imports as needed
so your custom implementation executes.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Add a derived text feature to the Transform stage.

For example, calculate the number of words
in a text field.

Verify that the resulting DataFrame
contains the new feature.

Explain what the feature measures
and how it might support analysis.

### Progression 3. Apply to a New Problem

Adapt the EVTL pipeline
to the JSONPlaceholder comments endpoint.

- Update the API URL in your custom configuration.
- Retrieve and inspect the JSON response.
- Identify the record structure and available fields.
- Update validation for the expected fields and data types.
- Modify Transform to extract at least three useful fields.
- Calculate at least one derived text feature.
- Save the resulting dataset to a CSV artifact.
- Verify that the output records are correct.
- Interpret what the resulting data represents.

Explain how the new JSON structure
differs from the original example.

The goal is to demonstrate that the pipeline
can be adapted to another structured data source
rather than relying on assumptions about one API.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- API source and analytical question.
- JSON structure and selected fields.
- Validation requirements.
- Transformation and derived features.
- Results and a relevant visual.
- Interpretation and limitations.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**.
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**.
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/nlp` folder reflects your authorship and custom work.
- [ ] The custom EVTL pipeline uses the new API data.
- [ ] The raw JSON and processed CSV artifacts are available.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
