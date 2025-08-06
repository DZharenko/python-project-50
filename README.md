### Hexlet tests and linter status:

[![Actions Status](https://github.com/DZharenko/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DZharenko/python-project-50/actions)
[![Python CI](https://github.com/DZharenko/python-project-50/actions/workflows/pyci.yaml/badge.svg)](https://github.com/DZharenko/python-project-50/actions/workflows/pyci.yaml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=DZharenko_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=DZharenko_python-project-50)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DZharenko_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DZharenko_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DZharenko_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DZharenko_python-project-50)
# Difference Calculator (gendiff)

- gendiff is a command-line tool for finding differences between files. This is the second project developed as part of
  the Hexlet course.

***

## Requirements:

[Python 3.12 +] - (https://www.python.org/downloads/)

[UV 0.6.14 +] - (https://astral.sh)
***

***

## Installation:

``` 
git clone git@github.com:DZharenko/python-project-50.git
```

````
cd python-project-50
````

`````
uv build
``````

````````
uv tool install dist/*.whl
````````

***

## Supported File Formats

#### - JSON (.json)

#### - YAML (.yaml, .yml)

***

## Usage

1. Place the files you want to compare inside the tests/test_data directory.
2. Run the following command, replacing file1 and file2 with your actual file names:

````
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
````

3. By default, the output is formatted using the 'stylish' formatter.

- To use a different format (json or plain), specify it with the -f flag:

***

### Example of tool output when using different formatters::

- **Default (stylish) formatter:**

````
uv run gendiff tests/test_data/<file1> tests/test_data/<file1>
````
[![Diff Stylish format asciicast](https://asciinema.org/a/TJL8c3xS36aRjJ4WjobKHccY1.svg)](https://asciinema.org/a/TJL8c3xS36aRjJ4WjobKHccY1)

- **Using the JSON formatter:**

``````
uv run gendiff -f json tests/test_data/<file1> tests/test_data/<file1>
``````
[![asciicast](https://asciinema.org/a/z9VeI2HObAfA616pAToNKbblC.svg)](https://asciinema.org/a/z9VeI2HObAfA616pAToNKbblC)

- **Using the Plain formatter:**

``````
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file1>
``````
[![Diff Plain format asciicast](https://asciinema.org/a/QDIe1HjLohqRMa3x1L4HqUXJd.svg)](https://asciinema.org/a/QDIe1HjLohqRMa3x1L4HqUXJd)


## Development and Testing
### Linting
Run ruff to check for linting issues:
```
make lint
```
Running Tests
```
make test-coverage
```

## Star this repo if you found it useful! :star: