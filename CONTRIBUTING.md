# Contributing to the XIL project
Contributions to the XIL project are warmly welcomed! Please read the following
guidelines before contributing.

# How to contribute?

## Issues

### Reporting bugs
If you find a bug or an outdated code that no longer works, please open an issue on the
project's issue tracker.
Make sure:
- The issue is not already reported by searching through the issues list.
- The issue is reproducible. Include steps to reproduce the issue.
- Include your local environment information, such as your operating system, your
  Python version, the version of the project you are using, etc.

### Suggesting enhancements
More than happy to hear your suggestions for improvements and new features. Please open
an issue on the project's issue tracker.

## Pull requests
Please open a pull request after you have opened an issue and discussed the changes
you want to make. This way we can make sure that the changes you want to make are
actually needed.

Code changes should be accompanied by tests. Make sure all the tests pass before opening
a pull request.  
If a test is a "live" test - i.e., it requires an internet connection - mark it with the
`live` pytest marker: `@pytest.mark.live`.

## Use the project
If you find the project useful, please consider starring it on GitHub. This will help
others find the project.

## Setting up the project locally
To set up the project on your computer, follow the steps below.

### Cloning the repository
Make sure you have [Git](https://git-scm.com/) installed and clone the repo:
```shell
git clone https://github.com/jond01/xil.git
```

### Python environment
#### Python version
This package supports specific versions of Python, with the latest version specified in
the [`.python-version` file](.python-version). Make sure you have at least this version
installed. You can use [pyenv](https://github.com/pyenv/pyenv) to manage multiple
Python versions.

If you use pyenv, install the specified Python version by running:
```shell
pyenv install
```
From the root of the project.

#### Virtual environment
To reproduce the exact Python environment used in this project, install
[uv](https://docs.astral.sh/uv/) (version specified in the
[constraint file](.github/workflows/uv-constraint.txt)) and run:
```shell
uv sync
```
from the root of the project.
To activate the uv virtual environment, run:
```shell
source .venv/bin/activate
```

### Pre-commit hooks
To validate your code before committing, install the pre-commit hooks:
```shell
pre-commit install
```
You need to run this command only once.
`pre-commit` is installed by uv when you run `uv sync`.

Every time you commit, the pre-commit hooks will run and validate your code to make
sure it complies with the project's standards. The hooks include the following
checks:
- `ruff`: code linting and formatting
- `mypy`: type checking
- `pylint`: code quality

The full list of hooks can be found in the `.pre-commit-config.yaml` file.

### Running the tests
To run the tests, run:
```shell
uv run pytest
```
Or simply `pytest` if you are in the activated virtual environment.
All the tests should pass. Make sure you run the tests before committing your code.

### Building the package

To build the package, run:
```shell
uv build
```

# Release workflow (for maintainers)

To release a new version, follow the steps below.

Issue a new *signed* tag locally:
```sh
git tag -s <version> -m "Release <version>"
```
Replace `<version>` with the version you want to release, e.g. `0.10.2` - without a `v`
prefix.

Push the tag to GitHub:
```sh
git push origin <version>
```

Run the [release workflow](https://github.com/jond01/xil/actions/workflows/release.yml) on GitHub Actions:
1. First choose `test-pypi`, and verify that the package is built and uploaded to
   TestPyPI:  
   https://test.pypi.org/project/xil/.  
   Download the wheel and verify the version number in the files:
   * `METADATA`
   * `xil/__init__.py`
2. Then choose `pypi`, and verify that the package is built and uploaded to PyPI:  
   https://pypi.org/project/xil/

After it's done - draft a new release on GitHub. Choose the tag you have just created:  
https://github.com/jond01/xil/releases/new

Hooray! We have a new release! 🎉
