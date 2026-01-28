import json

def task() -> float:

    with open("input.json") as f:
        json_data = json.load(f)

    sum_values = sum([i["score"] * i["weight"] for i in json_data])
    return round(sum_values, 3)

print(task())
