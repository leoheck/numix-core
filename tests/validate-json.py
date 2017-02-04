from jsonspec.validators import load
import json


with open('schema.json', 'r') as schema_obj:
    schema = schema_obj.read()
schema_obj.close()

validator = load(json.loads(schema))

with open('../data.json', 'r') as data_obj:
    data = data_obj.read()
data_obj.close()

validator.validate(json.loads(data))
