import json
from pathlib import Path

import yaml


def read_json(path_to_file):
    return json.load(open(path_to_file))


def read_yaml(path_to_file):
    with open(path_to_file, "r") as file:
        data = yaml.safe_load(file)
    return data
 

def get_test_file_path(filename):   
    return (Path(__file__).parent.parent.parent 
            / 'tests' 
            / 'test_data' 
            / filename)

