import json

def handle(n):
    empty_list = []
    a, b = 0, 1
    while a < 1000:
        a, b = b, a+b
        empty_list.append([a, b])
    return json.dumps({"list":empty_list, "input": n})
