import json

person_dict = { 'Name': 'Bob',
'Age': 12,
'Children': None
}

person_json = json.dumps(person_dict)

print(person_json)