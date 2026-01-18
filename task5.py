import json


FILENAME = "input.json"


def task() -> int:
    with open(FILENAME, encoding="utf-8") as f:
        data = json.load(f)

    total = sum(item["contains_improvement_appeals"] for item in data)
    return total


if __name__ == '__main__':
    print(task())
