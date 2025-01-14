import json

data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

with open('analyzed_data.json', 'w') as outfile:
    json.dump(data, outfile)
