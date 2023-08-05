"""Gendiff tests"""

from gendiff import generate_diff
import pytest

from fixtures.output import RIGHT_JSON, RIGHT_SIMPLE, RIGHT_STYLISH, RIGHT_PLAIN


@pytest.mark.parametrize("first_file, second_file, expected_output, format", [
    (
        './tests/fixtures/yaml/filepath1_plain.yml',
        './tests/fixtures/yaml/filepath2_plain.yml',
        RIGHT_SIMPLE,
        'stylish'
    ),
    (
        './tests/fixtures/json/file1_plain.json',
        './tests/fixtures/json/file2_plain.json',
        RIGHT_SIMPLE,
        'stylish'
    ),
    (
        './tests/fixtures/json/file1_nest.json',
        './tests/fixtures/json/file2_nest.json',
        RIGHT_STYLISH,
        'stylish'
    ),
    (
        './tests/fixtures/yaml/filepath1_nest.yml',
        './tests/fixtures/yaml/filepath2_nest.yml',
        RIGHT_STYLISH,
        'stylish'
    ),
    (
        './tests/fixtures/json/file1_nest.json',
        './tests/fixtures/json/file2_nest.json',
        RIGHT_PLAIN,
        'plain'
    ),
    (
        './tests/fixtures/yaml/filepath1_nest.yml',
        './tests/fixtures/yaml/filepath2_nest.yml',
        RIGHT_PLAIN,
        'plain'
    ),
    (
        './tests/fixtures/json/file1_nest.json',
        './tests/fixtures/json/file2_nest.json',
        RIGHT_JSON,
        'json'
    ),
    (
        './tests/fixtures/yaml/filepath1_nest.yml',
        './tests/fixtures/yaml/filepath2_nest.yml',
        RIGHT_JSON,
        'json'
    ),
])
def test_gendiff(first_file, second_file, expected_output, format):
    assert generate_diff(first_file, second_file, format) == expected_output
