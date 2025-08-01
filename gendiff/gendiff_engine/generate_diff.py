from gendiff.parse_file import read_json
from gendiff.parse_file import read_yaml
from .build_diff import build_diff
from .formatters import stylish_format, json_format
from pathlib import Path



def generate_diff(file_path1, file_path2, format_name='stylish'):

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

    
    result = build_diff(dict1, dict2)

    if format_name == 'stylish':
        result = stylish_format(result)
    elif format_name == 'json':
        result = json_format(result)  


    return result
