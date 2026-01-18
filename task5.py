def calculate_average_age(students):

    total_age = sum(student["age"] for student in students)
    average_age = total_age / len(students)
    return average_age


def filter_students_by_age(students, average_age):

    filtered_students = [student for student in students if student["age"] < average_age]
    return filtered_students



if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # Вычисление среднего возраста
    average_age = calculate_average_age(students_list)
    print("Средний возраст учеников:", average_age)

    # Фильтрация учеников по возрасту
    younger_students = filter_students_by_age(students_list, average_age)

    print("Список учеников с возрастом меньше среднего:")
    for current_student in younger_students:
        print(current_student['name'])
