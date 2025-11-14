import json
from functools import reduce

def handle(data):
    data = json.loads(data)
    result = {}
    for row in data["array_of_store"]:
      if row["region"] in result:
        result[row["region"]]["count"] += 1
      else:
        result[row["region"]] = {
          "count": 1,
          "child":{}
        }
    for row in data["array_of_store"]:
      if row["region2"] in result[row["region"]]["child"]:
        result[row["region"]]["child"][row["region2"]]["count"] += 1
        result[row["region"]]["child"][row["region2"]]["child"].append(row["address"])
      else:
        result[row["region"]]["child"][row["region2"]] = {
          "count": 1,
          "child":[row["address"]]
        }

    if data["store_stage"] == 1:
      buttons = list(result.keys())
    elif data["store_stage"] == 2:
      input = data["input"]
      item = result[input]
      if item["count"] == 1:
        item = next(iter(item["child"]))
        if len(item["child"]) == 1:
          buttons = []
        else:
          buttons = list(item["child"].keys())
      else:
        buttons = list(item["child"].keys())
    elif data["store_stage"] == 3:
      input = data["input"]

    return json.dumps({"buttons": buttons}, ensure_ascii=False)
handle(json_data)
