num_fields = int(input('num fields: '))
fields = []
for c in range(1, num_fields+1):
    field_name = str(input(f'Field name {c}: '))
    fields.append(field_name)


generated_json = {}
for field in fields:
    value = str(input(f'digite o valor do field {field}: '))
    generated_json[field] = value

import json as Json
print(Json.dumps(generated_json))


