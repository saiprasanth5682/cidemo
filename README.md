# Python CI Practice Project

A small Python project for learning GitHub Actions. It contains Python code,
unit tests, and one workflow that performs a basic build check and test run.

## Requirements

- Python 3.10 or newer
- No third-party Python packages are required

## Run locally

Run the application:

```bash
python app.py
```

Expected output:

```text
Hello, Vijay!
10 + 20 = 30
```

Build/syntax check:

```bash
python -m compileall -q .
```

Run unit tests:

```bash
python -m unittest discover -s tests -v
```

All five tests should pass.

## GitHub Actions

Workflow: `.github/workflows/ci.yml`

It runs when code is pushed to `main` or `D1`, and when a pull request
targets `main`.

The workflow checks out the code, sets up Python 3.12, compiles the Python
files as a basic build check, and runs unit tests with the built-in unittest
framework.

This is a CI learning example only. It does not deploy or release an application.
