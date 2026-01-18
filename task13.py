size = 9  # Размер таблицы умножения
for i in range(2, size+1):
    for j in range(2, size+1):
        result = i * j
        end = " " if j != size else ""  # Не печатать пробел для последнего столбца
        print(f"{result:2}", end=end)
    print()