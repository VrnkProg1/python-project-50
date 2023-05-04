import json
first_file = json.load(open('packages/modules/file1.json'))
second_file = json.load(open('packages/modules/file2.json'))


def generate_diff(first_file, second_file):
    first_file = json.load(open('packages/modules/file1.json'))
    second_file = json.load(open('packages/modules/file2.json'))
    dictionary_differences = {}
    for key in first_file.keys():
        if key in second_file.keys() and first_file["key"] == second_file["key"]:  # если ключ есть в обоих словарях и их значения равны
            dictionary_differences["key"] = first_file["key"]
        elif key not in second_file.keys():  # если ключ есть только в первом словаре
            dictionary_differences["-key"] = first_file["key"]
        elif key in second_file.keys():  # если ключ есть в обоих словарям, но значения не равны
            dictionary_differences["-key"] = first_file["key"]
            dictionary_differences["+key"] = second_file["key"]
        #sorted_tuple = sorted(dictionary_differences.items() , key=lambda x: x[0])
        return  dictionary_differences
