def build_diff(dict1, dict2):

    diff_result = []

    diff_keys = dict1.keys() | dict2.keys()
    sort_keys = sorted(diff_keys)

    for key in sort_keys:
        if key not in dict2:
            diff_result.append(
                {
                    'key': key,
                    'status': 'deleted',
                    'value': dict1[key],
                }     
            )
        elif key not in dict1:
            diff_result.append(
                {
                    'key': key,
                    'status': 'added',
                    'value': dict2[key],
                }
            )
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = build_diff(dict1[key], dict2[key])
            if nested_diff:
                diff_result.append(
                    {
                        'key': key,
                        'status': 'nested',
                        'children': nested_diff,
                    }
                )
        elif dict1[key] == dict2[key]:
            diff_result.append(
                {
                    'key': key,
                    'status': 'unchanged',
                    'value': dict1[key], 
                }
            )
        else:
            diff_result.append(
                {
                    'key': key,
                    'status': 'changed',
                    'value_old': dict1[key],
                    'value_new': dict2[key],
                }
            )
    return diff_result
