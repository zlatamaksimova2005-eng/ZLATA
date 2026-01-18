import json

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"


def task() -> None:
    with open(INPUT_FILE, "r", encoding="utf-8") as in_f:
        data = json.load(in_f)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_f:
        json.dump(data, out_f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    # Нужно для проверки задания
    task()

    with open(OUTPUT_FILE, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
