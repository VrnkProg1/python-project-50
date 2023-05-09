import json
first_file = json.load(open('packages/modules/file1.json'))
second_file = json.load(open('packages/modules/file2.json'))


def generate_diff(first_file, second_file):
    first_dict = json.load(open('packages/modules/file1.json'))
    second_dict = json.load(open('packages/modules/file2.json'))
    S = ''
    for key in sorted(first_dict):
        if key in first_dict and key in second_dict:  # если ключ из первого словаря есть во втором словаре
            if first_dict[key] == second_dict[key]:  # если значения равны
                S += f"  {key}: {first_dict[key]}\n"
            elif first_dict[key] != second_dict[key]:  # если значения не равны
                S += f"- {key}: {first_dict[key]}\n"
                S += f"+ {key}: {second_dict[key]}\n"
        if key not in second_dict and key in first_dict:  # если ключ из первого словаря отсутствует во втором словаре
            S += f"- {key}: {first_dict[key]}\n"
        if key not in first_dict and key in second_dict:  # если ключ из второго словаря отсутствует в первом словаре
            S += f"+ {key}: {second_dict[key]}\n"
    for key in sorted(second_dict):
        if key in second_dict and key not in first_dict:
            S += f"+ {key}: {second_dict[key]}"
    print(S.lower())


















    #for key in first_dict.keys():
        #if key in second_dict and first_dict[key] == second_dict[key]:  # если ключ есть в обоих словарях и их значения равны
            #print(f"  {key}: {first_dict[key]}")
        #if key not in second_dict and key in first_dict:  # если ключ есть только в первом словаре
            #print(f"- {key}: {first_dict[key]}")
        #if key in second_dict and key in first_dict and second_dict[key] != first_dict[key]:  # если ключ есть в обоих словарям, но значения не равны
            #print(f"- {key}: {first_dict[key]}")
            #print(f"+ {key}: {second_dict[key]}")
        #if key in second_dict and key not in first_dict:  #если ключ есть только во втором словаре
            #print(f"+ {key}: {second_dict[key]}")
        #if key in first_dict and key in second_dict:
            #if first_dict[key] == True and second_dict[key] == True:
            #    print(f"{key}: true")
            #elif first_dict[key] == True and second_dict[key] == False:
            #    print(f"- {key}: true")
            #    print(f"+ {key}: false")
            #elif first_dict[key] == False and second_dict[key] == True:
            #    print(f"- {key}: false")
            #    print(f"+ {key}: true")
            #elif first_dict[key] == False and second_dict[key] == False:
            #    print(f" {key}: false")
    #for key in second_dict.keys():
        #if key in second_dict and key not in first_dict:
            #print(f"+ {key}: {second_dict[key]}")
