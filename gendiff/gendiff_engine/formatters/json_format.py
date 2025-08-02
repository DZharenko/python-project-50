import json


def json_format(list_of_dicts):
    print(json.dumps(list_of_dicts, sort_keys=True, indent=4))

