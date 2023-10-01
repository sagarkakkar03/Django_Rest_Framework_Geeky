import json
python_data = {'name': 'Sagar', 'roll': 101}
json_data = json.dumps(python_data)
print(json_data)
parsed_data = json.loads(json_data)
print(parsed_data)