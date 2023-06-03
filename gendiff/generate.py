from gendiff.input_parser import parse_datafile


def generate_diff(first_file, second_file):
    first_dict = parse_datafile(first_file)
    second_dict = parse_datafile(second_file)
    print('{')
    result = {}
    for key in first_dict:
        if (key in second_dict) and second_dict[key] == first_dict[key]:
            result['  '+key] = first_dict[key]
            del second_dict[key]
        elif (key in second_dict) and second_dict[key] != first_dict[key]:
            result['- '+key] = first_dict[key]
            result['+ '+key] = second_dict[key]
            del second_dict[key]
        else:
            result['- '+key] = first_dict[key]
    for key in second_dict:
        result['+ '+key] = second_dict[key]
    result = dict(sorted(result.items(), key=lambda x: x[0][2]))
    for key in result:
        print(key, ':', result[key])
    print('}')
    return result
