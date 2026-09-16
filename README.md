# Python CLI CI/CD Showcase

![CI/CD Build Status](https://github.com/Akisolu/python-cli-ci-cd-showcase/actions/workflows/build.yml/badge.svg)

This repository demonstrates testing and automation practices in a Python project. The main focus is not the restaurant functionality itself, but how the code is validated, quality is protected, and delivery is automated with GitHub Actions.

The application is a small CLI for managing meals. Its most important aspect in this showcase is the quality infrastructure: tests, validation, and a continuous integration and delivery pipeline.

## Repository Goals

This project provides a practical example of:

- automated testing with `pytest`
- layered tests: unit, integration, and end-to-end
- validation of application logic and behavior
- automated execution with GitHub Actions
- executable artifact builds with PyInstaller
- automatic GitHub Release publishing

## Project Focus

The repository demonstrates how software quality is checked before a version is published:

- business functions are tested
- user flows are validated
- errors and retries are covered
- tests run for every change
- binaries are built only after the test pipeline succeeds

## Download and Run

To try the application without installing Python:

1. Open the **Releases** tab on GitHub and download the latest version for your operating system.
2. **Windows:** Run `restaurant_cli_windows.exe`.
3. **Linux:** Grant execute permission with `chmod +x restaurant_cli_linux`, then run `./restaurant_cli_linux`.

The CLI domain remains in Spanish so the example can model a Spanish-language application while its engineering documentation stays accessible to an international audience.

## Project Structure

```text
├── .github/
│   └── workflows/
│       └── build.yml                 # Main CI/CD workflow
├── src/
│   ├── crud.py                       # Data persistence logic
│   └── utils/
│   │   ├── comida.py                 # Pydantic meal model
│   │   ├── id_comida.py              # ID validation
│   │   └── input_menu.py             # Menu option validation
├── tests/
│   ├── units/                        # Unit tests
│   ├── integrations/                 # Integration tests
│   └── end-to-end/                   # End-to-end CLI tests
├── main.py                           # Application entry point
├── conftest.py                       # Pytest configuration
├── requirements.txt                  # Project dependencies
├── version                           # Project version
└── README.md                         # Repository documentation
```

## Testing Strategy

The `tests/` directory is the core of the project. It validates software quality at multiple levels.

### 1. Unit tests
Located in `tests/units/`.

These tests cover:

- JSON storage reads and writes
- record creation and deletion
- Pydantic validation
- invalid input handling
- isolated function behavior

Examples:

- `_cargar_datos()` returns an empty list when the file does not exist
- `crear_comida()` generates IDs correctly
- `eliminar_comida()` reports the actual operation result

### 2. Integration tests
Located in `tests/integrations/`.

These tests verify that the main application logic works with the data access layer and console interaction.

They cover scenarios such as:

- adding a meal through the main application logic
- displaying meals
- deleting a meal
- retrying after invalid input

### 3. End-to-end tests
Located in `tests/end-to-end/`.

These tests simulate the real terminal execution and verify the CLI end to end.

They cover flows such as:

- adding a meal and exiting
- entering an invalid option and continuing with a valid flow
- validating the expected console output

## Run Tests

Run the complete test suite with:

```bash
python -m pytest tests/ -v
```

Or use the project virtual environment:

```bash
.\.venv\Scripts\python.exe -m pytest tests/ -q
```

## Verified Status

The current test suite has been validated successfully with 64 passing tests:

```text
64 passed
```

This confirms that the project is working correctly from a quality and automation perspective.

## CI/CD Workflow

The automation is defined in `.github/workflows/build.yml` and is a key part of the project.

### Workflow Triggers

The workflow runs for these events:

- a `push` to the `main` branch
- a `pull_request` targeting `main`
- creation of tags matching `v*`

### Jobs

#### 1. Test job

This job performs:

- repository checkout
- Python setup across the configured version matrix
- dependency installation
- execution of the complete test suite

This prevents unvalidated changes from reaching the next stage.

#### 2. Build job

This job runs only after the tests pass.

It then:

- builds the application with PyInstaller
- creates executables on Windows and Ubuntu
- uploads the binaries as GitHub Actions artifacts

#### 3. Release job

This job runs only when a version tag is created.

It:

- downloads the generated artifacts
- creates a GitHub Release
- publishes the version binaries

## Tests and CI/CD

This project demonstrates a modern development workflow:

- changes are tested first
- the software is built next
- the final artifacts are generated
- the version is published only if the complete process succeeds

Automation is therefore a quality gate that validates the project before delivery.

## Technologies

- Python
- Pytest
- Pydantic
- PyInstaller
- GitHub Actions

## Summary

This repository is a practical example of automated QA and deployment pipelines. Although the app provides basic restaurant functionality, its main value is the project structure used to enforce quality with testing and continuous automation.

The central flow is:

```text
code -> tests -> validation -> build -> release
```

That is the workflow this project is designed to teach and demonstrate.
