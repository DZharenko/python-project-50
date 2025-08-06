import json

import yaml

from gendiff.gendiff_engine.parse_file import (
    get_test_file_path,
    read_json,
)


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