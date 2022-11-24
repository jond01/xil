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
This project uses Python 3.10 and above, make sure you have at least Python 3.10
installed. You can use [pyenv](https://github.com/pyenv/pyenv) to manage multiple
Python versions.

To reproduce the exact Python environment used in this project, install
[Poetry](https://python-poetry.org/) (version 1.2.2+) and run:
```shell
poetry install
```
from the root of the project.
To activate the Poetry virtual environment, run:
```shell
poetry shell
```

### Pre-commit hooks
To validate your code before committing, install the pre-commit hooks:
```shell
pre-commit install
```
You need to run this command only once.
`pre-commit` is installed by Poetry when you run `poetry install`.

Every time you commit, the pre-commit hooks will run and validate your code to make
sure it complies with the project's standards. The hooks include the following
checks:
- `black`: code formatting
- `mypy`: type checking
- `pylint`: code quality

The full list of hooks can be found in the `.pre-commit-config.yaml` file.

### Running the tests
To run the tests, run:
```shell
poetry run pytest
```
They should all pass. Make sure you run the tests before committing your code.
