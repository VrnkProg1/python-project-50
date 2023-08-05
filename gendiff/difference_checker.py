"""Function to check if there are differences between files."""

from gendiff.parsing import parse

from gendiff.formatters import format_selection

from gendiff.diff import find_diff


def generate_diff(first_file, second_file, format_name='stylish'):
    """
    Checking and generating differences between two files.
    The argument first_file is path to first file.
    The argument second_file is path to second file.
    The argument format_name is difference output format.
    """

    first_data, first_format = read_file(first_file)
    second_data, second_format = read_file(second_file)

    first_dict = parse(first_data, first_format)
    second_dict = parse(second_data, second_format)

    found_diff = find_diff(first_dict, second_dict)
    selected_format = format_selection(format_name)

    return selected_format(found_diff)


def read_file(file_name):
    """
    Accepts a filename.
    Returns the data of a file and its format.
    """

    with open(file_name, 'r') as file:
        file_data = file.read()
        fyle_format = file_name.split('.')[-1]
        return file_data, fyle_format
