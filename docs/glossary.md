# Glossary

This module focuses on acquiring and validating
structured data from web APIs using a modular pipeline.

## Quick Lookup

Common terms used in this module:

- **API** - an interface for communication between software systems.
- **Endpoint** - a network address that provides access to an API operation.
- **JSON** - a structured data interchange format.
- **Schema** - a definition of expected data structure and types.
- **Validation** - checking data against defined requirements.
- **Pipeline** - a sequence of data processing stages.
- **EVTL** - Extract, Validate, Transform, Load.

## API (Application Programming Interface)

An **API** defines how software systems
interact and exchange information.

A web API makes operations or data
available through network requests.

APIs allow applications to retrieve information
without directly accessing the underlying system.

## Endpoint

An **endpoint** is a network address
associated with a specific API operation or resource.

Different endpoints may provide
different data or functionality.

## HTTP Request

An **HTTP request** is a message
sent by a client to a web server.

Requests specify an operation
and may include headers, parameters,
and a request body.

Common HTTP methods include GET and POST.

## HTTP Response

An **HTTP response** is a message
returned by a server in response to an HTTP request.

Responses include a status code,
headers, and optionally a message body.

Status codes indicate outcomes
such as success, client errors, or server errors.

## JSON (JavaScript Object Notation)

**JSON** is a text-based format
for representing structured data.

JSON supports objects, arrays,
strings, numbers, booleans, and null values.

It is commonly used for data exchange
between web services and applications.

## JSON Object

A **JSON object** is a collection
of named values represented as key-value pairs.

JSON objects are commonly converted
to Python dictionaries during processing.

## JSON Array

A **JSON array** is an ordered collection
of values.

Arrays may contain objects, other arrays,
or primitive values.

## Record

A **record** is a collection of related
data fields representing one logical item.

Records are commonly represented
as objects or rows in a dataset.

## Schema

A **schema** defines the expected structure
of a dataset or data exchange format.

A schema may specify field names,
data types, required values,
and structural constraints.

## Data Validation

**Data validation** is the process
of checking whether data satisfies
defined structural and content requirements.

Validation may include checking:

- Required fields.
- Expected data types.
- Allowed values.
- Record structure.
- Missing or invalid data.

Passing validation establishes conformance
to the implemented checks,
not necessarily the accuracy of the source data.

## Pipeline

A **pipeline** is a sequence of processing stages
through which data is acquired, examined,
transformed, or stored.

Separating stages supports testing,
inspection, and maintenance.

## EVTL (Extract, Validate, Transform, Load)

**EVTL** is a pipeline architecture
that separates processing into four stages:

- **Extract** - acquire data from a source.
- **Validate** - check data against defined requirements.
- **Transform** - convert data into a useful representation.
- **Load** - write data to a destination.

The explicit Validate stage makes
data quality checks visible
before further processing.

## Source

A **source** is the origin of data
used by a pipeline or processing stage.

Sources may include APIs, files,
databases, or other systems.

## Sink

A **sink** is a destination
that receives processed data.

Sinks may include files, databases,
message queues, or other storage systems.

## Transformation

**Data transformation** changes the structure,
representation, or values of data.

Transformations may include selecting fields,
converting types, standardizing values,
or calculating derived fields.

## Derived Field

A **derived field** is a value calculated
from existing data rather than obtained
directly from the original source.

Derived fields support additional
analysis and interpretation.

## Reproducibility

**Reproducibility** is the ability
to repeat a computational process
under defined conditions
and obtain consistent results.

Reproducibility depends on controlling
inputs, configuration, dependencies,
and relevant execution conditions.

---

[◄ Back to 🏠 Home](index.md)
