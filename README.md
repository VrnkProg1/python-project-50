### Hexlet tests and linter status:
![Python CI](https://github.com/VrnkProg1/python-project-50/workflows/Python%20CI/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/f44ace4ea5edd04d05ec/maintainability)](https://codeclimate.com/github/VrnkProg1/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f44ace4ea5edd04d05ec/test_coverage)](https://codeclimate.com/github/VrnkProg1/python-project-50/test_coverage)

# Gendiff

The second project written for the academic purposes of a Hexlet's course on learning a programming language Python.

## About the project

Gendiff is the Difference Generator is a program that looks for differences between two files.

- Suppported formats: YAML, JSON
- The following output formats are available: json, plaind and stylish
- Can be used as CLI tool or library

## How to install and use

### Install
`python3 -m pip install git+https://github.com/VrnkProg1/python_project-50`

### Use as a library
```
from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2, format_name)
print(diff)
```
Default argument for format format_name='stylish'

### Use as a CLI
```
gendiff -h
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

## Demonstration of the program

### Asciinema format stylish for flat json files
[![asciicast](https://asciinema.org/a/YtuxqVpFyiruXDKDt3Mbna5o4.svg)](https://asciinema.org/a/YtuxqVpFyiruXDKDt3Mbna5o4)

### Asciinema format stylish for flat yaml files
[![asciicast](https://asciinema.org/a/JpGz55ZyrhOT7oC290x0C3K75.svg)](https://asciinema.org/a/JpGz55ZyrhOT7oC290x0C3K75)

### Asciinema format stylish for json and yaml files has nested structures
[![asciicast](https://asciinema.org/a/rEdIvhW2zNCbVXwj1d5btUSLe.svg)](https://asciinema.org/a/rEdIvhW2zNCbVXwj1d5btUSLe)

### Asciinema format plain for json and yaml files has nested structures
[![asciicast](https://asciinema.org/a/4DVtlOUEq8JDHDRMVmAWDKOmt.svg)](https://asciinema.org/a/4DVtlOUEq8JDHDRMVmAWDKOmt)

### Asciinema format json for json files has nested structures
[![asciicast](https://asciinema.org/a/7za9m8Hwd3KBxuVOBSnNTEYoA.svg)](https://asciinema.org/a/7za9m8Hwd3KBxuVOBSnNTEYoA)