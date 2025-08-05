def get_formatted_value(value):
    if value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain_format(list_of_dicts, parents=None, result=None):
    
    if result is None:
        result = []

    for elem in list_of_dicts:
        
        key_name = elem['key']
        value_current = get_formatted_value(elem.get('value'))
        value_old = get_formatted_value(elem.get('value_old'))
        value_new = get_formatted_value(elem.get('value_new'))
        status = elem['status']

        parent = f'{parents}.{key_name}' if parents else key_name

        if status == 'added':
            result.append(f"Property '{parent}' was added with value: \
                          {value_current}")

        elif elem.get('status') == 'deleted':
            result.append(f"Property '{parent}' was removed")
        
        elif elem.get('status') == 'changed':
            result.append(f"Property '{parent}' was updated. \
                          From {value_old} to {value_new}")

        elif status == 'nested':
            plain_format(elem.get('children'), parent, result)                
        
    return '\n'.join(result)

