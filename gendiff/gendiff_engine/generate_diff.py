from gendiff.parse_file import read_json

def generate_diff(file_path1, file_path2):
        
    dict1 = read_json(file_path1)
    dict2 = read_json(file_path2)

    result = '' 

    diff_keys = dict1.keys()|dict2.keys()
    sort_keys = sorted(list(diff_keys))
    
    for key in sort_keys:
        if key in dict1 and  key in dict2:
            if dict1[key] == dict2[key]:
                result += f" {key}: {dict1[key]} \n" 
            else:
                result += f"- {key}: {dict1[key]} \n" + \
                          f"+ {key}: {dict2[key]} \n" 
                                         
        if key in dict1 and key not in dict2:
            result += f"- {key}: {dict1[key]} \n"
        elif key not in dict1 and key in dict2:
            result += f"- {key}: {dict2[key]} \n"

    return "{ \n" + result + "}"