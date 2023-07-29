"""Function for displaying differences in a stylish format"""

import json

from gendiff.consts import (
    DELETED,
    ADDED,
    NESTED,
    UNCHANGED
)

NEW = '+'
OLD = '-'
NOCHANGE = ' '
NUMBER_OF_SPACES = 4
SPACE = ' '
TEMPLATE_STYLISH = '{0}{1} {2}: {3}'


def format(tree, depth=1):
    """
    Difference output in stylish format.
    The argument tree is difference tree of two files.
    The argument depth is the current depth of the tree traversal.
    Returns a list where all differences are described.
    """

    output = ['{']
    start_space = calculate_space(depth).get('start')
    end_space = calculate_space(depth).get('end')

    for item in tree:
        type_node = item.get('type')
        key = item.get('key')
        first_value = item.get('first_value')
        second_value = item.get('second_value')
        complex = item.get('nested')

        if type_node is DELETED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, OLD, key,
                to_string(first_value, depth + 1)
            ))
        elif type_node is ADDED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, NEW, key,
                to_string(second_value, depth + 1)
            ))
        elif type_node is UNCHANGED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, NOCHANGE, key,
                to_string(first_value, depth + 1)
            ))
        elif type_node is NESTED:
            output.append(TEMPLATE_STYLISH.format(
                start_space, NOCHANGE, key,
                format(complex, depth + 1)
            ))
        else:
            output.append(TEMPLATE_STYLISH.format(
                start_space, OLD, key,
                to_string(first_value, depth + 1)
            ))
            output.append(TEMPLATE_STYLISH.format(
                start_space, NEW, key,
                to_string(second_value, depth + 1)
            ))

    output.append(end_space + '}')
    return '\n'.join(output)


def calculate_space(depth):
    """
    Calculates the space you need to have before and after the node.
    """

    space = {'start': SPACE * (NUMBER_OF_SPACES * depth - 2),
             'end': SPACE * (NUMBER_OF_SPACES * (depth - 1))}

    return space


def to_string(value, depth):
    """
    Checks if the value is complex.
    Converts the value to the desired output format.
    """

    result = []
    start_space = calculate_space(depth).get('start')
    end_space = calculate_space(depth).get('end')

    if isinstance(value, dict):
        result.append('{')
        for key, leaf_value in value.items():
            result.append(TEMPLATE_STYLISH.format(
                start_space, NOCHANGE,
                key, to_string(leaf_value, depth + 1)
            ))

        result.append(end_space + '}')
    elif isinstance(value, str):
        result.append(value)
    else:
        result.append(json.dumps(value))
    return '\n'.join(result)
