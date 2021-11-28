# Dependencies for Sublime Text Linters and Formatters

Install dependencies for [Sublime Text](https://www.sublimetext.com/) linters and formatters and
generate the necessary configurations.

Sublime Text linters and formatters don't install their dependencies. This project installs them and
generates the configurations pointing at the installation locations.

## Prerequisites

- [Python](https://www.python.org/)
- [Volta](https://volta.sh/)
- [Sublime Text 4](https://www.sublimetext.com/)
    - [sublack](https://github.com/jgirardet/sublack)
    - [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter)
        - [SublimeLinter-flake8](https://github.com/SublimeLinter/SublimeLinter-flake8)
        - [SublimeLinter-contrib-xo](https://github.com/xojs/SublimeLinter-contrib-xo)

If installed [pyenv](https://github.com/pyenv/pyenv) will be used to install the right Python version.

## Installation

Run `make` to install or update all dependencies listed below:

- [black](https://github.com/ambv/black)
- [flake8](https://gitlab.com/pycqa/flake8)
    - [flake8-bandit](https://github.com/tylerwince/flake8-bandit)
    - [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
    - [flake8-builtins](https://github.com/gforcada/flake8-builtins)
    - [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
    - [flake8-debugger](https://github.com/JBKahn/flake8-debugger)
    - [flake8-docstrings](https://gitlab.com/pycqa/flake8-docstrings)
    - [flake8-eradicate](https://github.com/sobolevn/flake8-eradicate)
    - [flake8-isort](https://github.com/gforcada/flake8-isort)
    - [flake8-logging-format](https://github.com/globality-corp/flake8-logging-format)
    - [flake8-tidy-imports](https://github.com/adamchainz/flake8-tidy-imports)
    - [pep8-naming](https://github.com/PyCQA/pep8-naming)
- [xo](https://github.com/xojs/xo)

## Linters

Use this command to configure the flake8 and xo linters:

```console
./configure.py sublimelinter
```

Add the JSON output to your SublimeLinter settings.

## Formatters

### sublack

Use this command to configure the sublack package:

```console
./configure.py sublack
```

Add the JSON output to your sublack settings.

## License

Distributed under the 3-clause BSD license.

Copyright 2021 Markus Zapke-Gründemann
