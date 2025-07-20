from gendiff.parse_file import read_json
from gendiff.parse_file import read_yaml
from pathlib import Path  


def generate_diff(file_path1, file_path2):

    file1_path = Path(file_path1)
    file2_path = Path(file_path2)  

    file1_name = file1_path.name
    file2_name = file2_path.name

    file1_extension = file1_name.split('.')[1]
    file2_extension = file2_name.split('.')[1]
    
    if file1_extension == 'json':
        dict1 = read_json(file_path1)
    elif file1_extension == 'yaml' or file1_extension == 'yml' :
        dict1 = read_yaml(file_path1)

    if file2_extension == 'json':
        dict2 = read_json(file_path2)
    elif file2_extension == 'yaml' or file2_extension == 'yml':
        dict2 = read_yaml(file_path2)

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


