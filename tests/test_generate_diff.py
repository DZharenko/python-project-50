import json
from pathlib import Path

import yaml

# from gendiff.scripts.generate_diff import generate_diff
from gendiff.gendiff_engine.generate_diff import generate_diff
# from gendiff.scripts.parsing_file import  get_parsed_file, read_json, read_yaml
from gendiff.gendiff_engine.parse_file import read_json, read_yaml, get_test_file_path


# def get_test_data_path(filename):
#     return Path(__file__).parent / 'test_data' / filename


def read_text_file(filename):
    return get_test_file_path(filename).read_text()


def read_json_file(filename):
    with open(get_test_file_path(filename), 'r') as file:
        return json.load(file)


def read_yaml_file(filename):
    with open(get_test_file_path(filename), 'r') as file:
        return yaml.safe_load(file)


def test_parsing_json():
    file1_json = get_test_file_path('file1.json')
    expected = read_json_file('file1.json')

    assert read_json(file1_json) == expected