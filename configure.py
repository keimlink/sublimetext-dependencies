#!/usr/bin/env python3
"""Confgure Sublime Text packages and print the configuration as JSON."""
import argparse
import json
import pathlib


def configure_flake8(python):
    """Confgure the Flake8 linter."""
    extend_ignore = [
        "A003",  # "attribute" is a python builtin, consider renaming the class attribute
        "D100",  # Missing docstring in public module
        "D105",  # Missing docstring in magic method
        "D106",  # Missing docstring in public nested class
        # Options related to Black and flake8-bugbear
        # https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#flake8
        # https://github.com/PyCQA/flake8-bugbear#how-to-enable-opinionated-warnings
        "E203",  # whitespace before ':' - warning is not PEP 8 compliant
        "E501",  # line too long (82 > 79 characters) - must be disabled for B950 to be hit
        "W503",  # line break before binary operator - warning is not PEP 8 compliant
    ]
    extend_select = [
        "A",  # flake8-builtins
        "B",  # flake8-bugbear
        "B9",  # flake8-bugbear opinionated warnings
        "C",  # flake8-comprehensions, mccabe
        "D",  # flake8-docstrings
        # "DJ",  # flake8-django
        "G",  # flake8-logging-format
        "I",  # flake8-isort, flake8-tidy-imports
        "N",  # pep8-naming
        "S",  # flake8-bandit
        "T",  # flake8-debugger
    ]
    per_file_ignores = {
        "test_*.py": [
            "D101",  # Missing docstring in public class
            "D102",  # Missing docstring in public method
            "D103",  # Missing docstring in public function
            "S101",  # Use of assert detected.
        ],
        "tests/*__init__.py": [
            "D104",  # Missing docstring in public package
        ],
    }
    return {
        "args": [
            "--extend-ignore",
            ",".join(extend_ignore),
            "--extend-select",
            ",".join(extend_select),
            "--max-complexity",
            "10",
            "--max-line-length",
            "99",
            "--per-file-ignores",
            " ".join(
                [f"{filename}:{','.join(errors)}" for filename, errors in per_file_ignores.items()]
            ),
            "--stdin-display-name",
            "${file:stdin}",  # Make source filename available to flake8, use stdin as fallback
        ],
        "python": python,
    }


def configure_xo(node_modules):
    """Confgure the xo linter."""
    return {
        "args": ["--env", "browser", "--space", "4"],
        "executable": node_modules / ".bin" / "xo",
        "selector": "source.js - meta.attribute-with-value - source.js.embedded.html",
    }


def configure_sublimelinter(cwd):
    """Confgure linters for the SublimeLinter package."""
    python = cwd / ".venv" / "bin" / "python"
    node_modules = cwd / "node_modules"
    return {
        "linters": {
            "flake8": configure_flake8(python),
            "xo": configure_xo(node_modules),
        }
    }


def configure_sublack(cwd):
    """Confgure the sublack package."""
    return {
        "black_line_length": 99,
        "black_command": cwd / ".venv" / "bin" / "black",
        "black_use_blackd": True,
        "black_blackd_autostart": True,
    }


class JSONPathlibEncoder(json.JSONEncoder):
    """JSON encoder for pathlib objects."""

    def default(self, obj):
        """Encode any pathlib.Path object to a string."""
        if isinstance(obj, pathlib.Path):
            return str(obj)
        return super.default(obj)


def serialize(configuration):
    """Serialize configuration as JSON string representation."""
    return JSONPathlibEncoder(indent=4).encode(configuration)


def configure(packages):
    """Confgure a Sublime Text package and print the configuration as JSON."""
    parser = argparse.ArgumentParser(description=configure.__doc__)
    parser.add_argument("package", choices=packages, help="Name of package to be configured")
    args = parser.parse_args()
    configuration = packages[args.package](pathlib.Path.cwd())
    print(serialize(configuration))


if __name__ == "__main__":
    packages = {"sublack": configure_sublack, "sublimelinter": configure_sublimelinter}
    configure(packages)
