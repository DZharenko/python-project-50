from gendiff.parse_file import read_json


def generate_diff(file_path1, file_path2):
        
    dict1 = read_json(file_path1)
    dict2 = read_json(file_path2)

    result = [] 

    diff_keys = dict1.keys() | dict2.keys()
    sort_keys = sorted(list(diff_keys))

    for key in sort_keys:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result.append(f"    {key}: {dict1[key]}")
            else:
                result.append(f"  - {key}: {dict1[key]}")
                result.append(f"  + {key}: {dict2[key]}") 
                                         
        if key in dict1 and key not in dict2:
            result.append(f"  - {key}: {dict1[key]}")
        
        if key not in dict1 and key in dict2:
            result.append(f"  - {key}: {dict2[key]}")
       
    return "{\n" + '\n'.join(result) + "\n}"
