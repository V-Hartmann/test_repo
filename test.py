import json

def handle(n):
    empty_list = []
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
        empty_list.append([a, b])
    return json.dumps({"list":empty_list})
