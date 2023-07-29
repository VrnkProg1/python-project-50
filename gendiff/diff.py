"""Finding differences between two dictionaries."""

from gendiff.consts import (
    ADDED,
    DELETED,
    NESTED,
    UNCHANGED,
    CHANGED
)


def find_diff(fisrt_dict, second_dict):
    """
    Takes two dictionaries as arguments and finds differences between them.
    The argument first_dict is first dictionary.
    The argument second_dict is second dictionary.
    Returns a tree of differences.
    """

    first_keys = fisrt_dict.keys()
    second_keys = second_dict.keys()
    all_keys = first_keys | second_keys
    tree = []

    for key in sorted(all_keys):
        if key not in fisrt_dict:
            ast = {'type': ADDED, 'key': key,
                   'second_value': second_dict.get(key)
                   }
        elif key not in second_dict:
            ast = {'type': DELETED, 'key': key,
                   'first_value': fisrt_dict.get(key)
                   }
        elif fisrt_dict.get(key) == second_dict.get(key):
            ast = {'type': UNCHANGED, 'key': key,
                   'first_value': fisrt_dict.get(key)
                   }
        elif isinstance(
            fisrt_dict.get(key), dict) and isinstance(
                second_dict.get(key), dict):
            ast = {'type': NESTED, 'key': key,
                   'nested': find_diff(fisrt_dict.get(key),
                                       second_dict.get(key)
                                       )}
        else:
            ast = {'type': CHANGED, 'key': key,
                   'first_value': fisrt_dict.get(key),
                   'second_value': second_dict.get(key)
                   }
        tree.append(ast)
    return tree
