def get_shortest_word(words_list):

    if not words_list:
        return None
    return min(words_list, key=len)


if __name__ == "__main__":
    words_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
    shortest_word = get_shortest_word(words_list)  # Найдите самое короткое слово
    print(shortest_word)  # kiwi
