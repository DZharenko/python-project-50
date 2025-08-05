def get_shift(depth, replacer=' '):
    return replacer * (depth * 4 - 2)


def get_formatted_value(value, depth=1):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        shift = get_shift(depth + 1)
        result = []
        for key, val in value.items():
            formatted_value = get_formatted_value(val, depth + 1)
            result.append(f"{shift}  {key}: {formatted_value}")
        return "{{\n{}\n{}}}".format("\n".join(result), shift[:-2])
    return f"{value}"


def stylish_format(list_of_dicts, depth=1):
    shift = get_shift(depth)
    result = []

    for elem in list_of_dicts:
        
        key_name = elem['key']
        value_current = get_formatted_value(elem.get('value'), depth)
        value_old = get_formatted_value(elem.get('value_old'), depth)
        value_new = get_formatted_value(elem.get('value_new'), depth)
        status = elem['status']

        if status == 'added':
            result.append(f'{shift}+ {key_name}: {value_current}')

        elif status == 'nested':
            children = stylish_format(elem.get('children'), depth + 1)
            result.append(f'{shift}  {key_name}: {children}')

        elif elem.get('status') == 'deleted':
            result.append(f'{shift}- {key_name}: {value_current}')
        
        elif elem.get('status') == 'unchanged':
            result.append(f'{shift}  {key_name}: {value_current}')
        
        elif elem.get('status') == 'changed':
            result.append(f'{shift}- {key_name}: {value_old}')
            result.append(f'{shift}+ {key_name}: {value_new}')                
        
    return "{{\n{}\n{}}}".format("\n".join(result), shift[:-2])
