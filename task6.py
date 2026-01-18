import json


FILENAME = "input.json"


def task() -> dict:
    with open(FILENAME, encoding="utf-8") as f:
        data = json.load(f)

    max_dict = max(data, key=lambda x: x["score"])
    return max_dict


if __name__ == '__main__':
    print(task())
