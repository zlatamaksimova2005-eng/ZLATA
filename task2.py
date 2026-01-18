INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, "r", encoding="utf-8") as in_file, \
            open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:

        for line in in_file:
            out_file.write(line.upper())


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILE) as file:
        for current_line in file:
            print(current_line, end="")
