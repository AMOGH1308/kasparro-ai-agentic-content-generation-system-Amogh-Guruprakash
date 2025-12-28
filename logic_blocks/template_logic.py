import json

def fill_template(template: dict, data: dict):
    result = {}

    for key, val in template.items():

        # Case 1: placeholder wants a dict or list
        if isinstance(val, str) and val == "{questions}":
            result[key] = data["questions"]   # insert as dict
            continue

        # Case 2: normal string placeholders
        if isinstance(val, str):
            result[key] = val.format(**data)
        else:
            result[key] = val

    return result
