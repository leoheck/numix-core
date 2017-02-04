from jsonspec.validators import load, exceptions
import json


with open('schema.json', 'r') as schema_obj:
    schema = schema_obj.read()
schema_obj.close()

validator = load(json.loads(schema))

with open('../data.json', 'r') as data_obj:
    data = data_obj.read()
data_obj.close()

try:
    validator.validate(json.loads(data))
except jsonspec.validators.exceptions.ValidationError:
    exit("The json file is not following the correct schema.")
