# Your first line of Python code
import json

def handle(input_data):
    input_data = json.loads(input_data)
    
    return json.dump(input_data)
