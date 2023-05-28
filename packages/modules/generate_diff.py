import json


def generate_diff(first_file, second_file):
    first_dict = json.load(open('packages/modules/file1.json'))
    second_dict = json.load(open('packages/modules/file2.json'))
    list_of_keys = {}
    for key in first_dict:
        list_of_keys[key] = None
    for key in second_dict:
        list_of_keys[key] = None
    sorted_list = '{'
    sorted_list += '\n'
    for key in sorted(list_of_keys):
        if first_dict.get(key) is True or first_dict.get(key) is False:  # если булево значение в первом словаре  # noqa: E501
            if first_dict[key] is True:
                sorted_list += f"  - {key}: true\n"
            elif first_dict[key] is False:
                sorted_list += f"  - {key}: false\n"
            continue
        elif second_dict.get(key) is True or second_dict.get(key) is False:  # если булево значение во втором словаре  # noqa: E501
            if second_dict[key] is True:
                sorted_list += f"  + {key}: true\n"
            elif second_dict[key] is False:
                sorted_list += f"  + {key}: false\n"
            continue
        if key in first_dict and key in second_dict:  # если ключ из первого словаря есть во втором словаре  # noqa: E501
            if first_dict[key] == second_dict[key]:  # если значения равны
                sorted_list += f"    {key}: {first_dict[key]}\n"
            elif first_dict[key] != second_dict[key]:  # если значения не равны
                sorted_list += f"  - {key}: {first_dict[key]}\n"
                sorted_list += f"  + {key}: {second_dict[key]}\n"
            continue
        if key not in second_dict and key in first_dict:  # если ключ из первого словаря отсутствует во втором словаре  # noqa: E501
            sorted_list += f"  - {key}: {first_dict[key]}\n"
        if key not in first_dict and key in second_dict:  # если ключ из второго словаря отсутствует в первом словаре  # noqa: E501
            sorted_list += f"  + {key}: {second_dict[key]}\n"
    sorted_list += "}"
    print(sorted_list)
