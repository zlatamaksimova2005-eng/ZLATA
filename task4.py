def calculate_parking_load(total_parking_spaces, occupied_parking_spaces):

    load_percentage = (occupied_parking_spaces / total_parking_spaces) * 100
    return round(load_percentage)

print(calculate_parking_load(100, 75))  # Вывод: 75

print(calculate_parking_load(50, 25))  # Вывод: 50

print(calculate_parking_load(200, 150))  # Вывод: 75
