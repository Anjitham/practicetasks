dict = {'a': 1, 'b': 2, 'c': 3}

key_to_check= 'd'

if key_to_check in dict:
    result = dict[key_to_check]
else:
    result = f"Key '{key_to_check}' not found."

print(result)