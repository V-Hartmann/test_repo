import json

def handle(data):
    data = json.loads(data)
    data = json.dumps({"data": data})

    return data
