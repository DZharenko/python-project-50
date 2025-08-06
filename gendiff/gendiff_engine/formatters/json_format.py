import json


def json_format(list_of_dicts):
    return (json.dumps(list_of_dicts, sort_keys=True, indent=4))

