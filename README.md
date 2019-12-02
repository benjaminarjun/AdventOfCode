# AdventOfCode

Solutions to the Advent of Code problems: https://adventofcode.com. The problems are solved in both Python and Rust. A quick guide to each:

## Python

The root directory for the Python component of the project is `{projectRoot}/python`. The `solutions` folder contains a
subfolder for each day, as well as modules to store shared utilities. The code written specifically to solve a particular
day's puzzle will be stored in `{projectRoot}/python/solutions/day{N}`.

### Setting up an environment

A virtual environment can be created by running the command `python3 -m venv` in the Python root directory. To activate the
environment, run `source env/bin/activate`. Then run `pip install -r requirements.txt` to install dependencies.

### Running solutions

The information requested by the puzzle will be output by the `releases.py` file in a given day's folder. To run the file,
execute `python -m solutions.day{N}.results` from the Python root.

### Running tests

This project uses `unittest`. Run tests with `python -m unittest solutions.day{N}.test_lib` (this will likely change in the
near future).

## Rust

Coming soon!
