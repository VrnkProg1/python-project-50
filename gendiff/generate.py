from gendiff.input_parser import parse_datafile


def check_for_bool(key_value, dict):
    if isinstance(dict[key_value], bool):
        value = str(dict[key_value]).lower()
    return value


def generate_diff(first_file, second_file):
    first_dict = parse_datafile(first_file)
    second_dict = parse_datafile(second_file)
    print('{')
    result = {}

    # for key in keys:
    #     value1 = dict1.get(key)
    #     value2 = dict2.get(key)

    #     if isinstance(value1, dict) and isinstance(value2, dict):
    #         nested_result = {}
    #         find_differences(value1, value2, nested_result, parent_key + key + ".")
    #         if nested_result:
    #             result_dict[parent_key + key] = nested_result
    #     elif value1 != value2:
    #         if value1 is None:
    #             result_dict[parent_key + key] = "+ " + str(value2)
    #         elif value2 is None:
    #             result_dict[parent_key + key] = "- " + str(value1)
    #         else:
    #             result_dict[parent_key + key] = "- " + str(value1)
    #             result_dict[parent_key + key] = "+ " + str(value2)



    for key in first_dict:
        if (key in second_dict) and second_dict[key] == first_dict[key]:
            if isinstance(first_dict[key], bool):
                value = str(first_dict[key]).lower()
                result['  '+key] = value
            else:
                result['  '+key] = first_dict[key]
            del second_dict[key]
        elif (key in second_dict) and second_dict[key] != first_dict[key]:
            if isinstance(first_dict[key], bool):
                value = str(first_dict[key]).lower()
                result['- '+key] = value
            else:
                result['- '+key] = first_dict[key]
            if isinstance(second_dict[key], bool):
                value = str(second_dict[key]).lower()
                result['+ '+key] = value
            else:
                result['+ '+key] = second_dict[key]
            del second_dict[key]
        else:
            if isinstance(first_dict[key], bool):
                value = str(first_dict[key]).lower()
                result['- '+key] = value
            else:
                result['- '+key] = first_dict[key]
    for key in second_dict:
        if isinstance(second_dict[key], bool):
            value = str(second_dict[key]).lower()
            result['+ '+key] = value
        else:
            result['+ '+key] = second_dict[key]
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    for key in result:
        print(key, ':', result[key])
    print('}')
    return result
    