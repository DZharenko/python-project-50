import json
import yaml

from pathlib import Path


def read_json(path_to_file):
    return json.load(open(path_to_file))

def read_yaml(path_to_file):
    with open(path_to_file, "r") as file:
        data = yaml.safe_load(file)
    return data
 
def get_test_file_path(filename):   
    return Path(__file__).parent.parent / 'tests' / 'test_data' / filename


# print(read_yaml(get_test_file_path('file2.yaml')))
# print(read_yaml(get_test_file_path('file1.json')))