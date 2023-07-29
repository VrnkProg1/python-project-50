"""Function for displaying differences in a plain format"""

import json

from gendiff.consts import (
    DELETED,
    ADDED,
    NESTED,
    CHANGED
)

TEMPLATE_ADDED = "Property '{0}' was added with value: {1}"
TEMPLATE_REMOVED = "Property '{0}' was removed"
TEMPLATE_UPDATED = "Property '{0}' was updated. From {1} to {2}"


def format(tree, path=[]):
    """
    Difference output in plain format.
    The argument tree is difference tree of two files.
    The argument path is the path to the value.
    Returns a list where all differences are described.
    """

    output = []
    for item in tree:
        type_node = item.get('type')
        key = item.get('key')
        first_value = item.get('first_value')
        second_value = item.get('second_value')
        complex = item.get('nested')

        path.append(key)

        if type_node is DELETED:
            output.append(TEMPLATE_REMOVED.format('.'.join(path)))
        elif type_node is ADDED:
            output.append(TEMPLATE_ADDED.format('.'.join(path),
                                                to_string(second_value)))

        elif type_node is CHANGED:
            output.append(TEMPLATE_UPDATED.format('.'.join(path),
                                                  to_string(first_value),
                                                  to_string(second_value)))
        elif type_node is NESTED:
            output.append(format(complex, path))
        path.pop()

    return '\n'.join(output)


def to_string(value):
    """
    Converting the value to the desired format.
    """

    if isinstance(value, str):
        result = f"'{value}'"
    elif isinstance(value, dict):
        result = '[complex value]'
    else:
        result = json.dumps(value)

    return result
