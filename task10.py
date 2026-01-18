def calculate_average_age(students_dict):
    ages = students_dict.values()
    average_age = sum(ages) / len(ages)
    return average_age

students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

average_age = calculate_average_age(students_dict)
print(f"Средний возраст студентов: {average_age}")
