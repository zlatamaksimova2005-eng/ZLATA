import doctest
from typing import Optional, List


class BankAccount:
    """
    Класс, представляющий банковский счет.

    Атрибуты:
    - account_number: str - номер счета
    - balance: float - текущий баланс
    - currency: str - валюта счета
    """

    def __init__(self, account_number: str, balance: float, currency: str):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param balance: Начальный баланс
        :param currency: Валюта счета

        Примеры:
        >>> account = BankAccount("40817810099910004312", 5000.0, "RUB")
        >>> account.account_number
        '40817810099910004312'
        >>> account.balance
        5000.0
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if len(account_number) < 10:
            raise ValueError("Номер счета должен содержать минимум 10 символов")
        self.account_number = account_number

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = float(balance)

        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть строкой")
        if len(currency) != 3:
            raise ValueError("Валюта должна состоять из 3 символов (например, RUB, USD)")
        self.currency = currency.upper()

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета.

        :param amount: Сумма для пополнения

        :raise ValueError: Если сумма пополнения отрицательная или нулевая

        Примеры:
        >>> account = BankAccount("40817810099910004312", 5000.0, "RUB")
        >>> account.deposit(1000.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма пополнения должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        # Реализация метода (для прохождения теста)
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия

        :return: Успешность операции (True если достаточно средств, False если нет)

        :raise ValueError: Если сумма снятия отрицательная или нулевая

        Примеры:
        >>> account = BankAccount("40817810099910004312", 5000.0, "RUB")
        >>> account.withdraw(1000.0)
        True
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма снятия должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        # Реализация метода (для прохождения теста)
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account: 'BankAccount', amount: float) -> bool:
        """
        Перевод денег на другой счет.

        :param target_account: Целевой счет для перевода
        :param amount: Сумма перевода

        :return: Успешность операции

        Примеры:
        >>> account1 = BankAccount("40817810099910004312", 5000.0, "RUB")
        >>> account2 = BankAccount("40817810099910004313", 1000.0, "RUB")
        >>> account1.transfer(account2, 1000.0)
        True
        """
        if not isinstance(target_account, BankAccount):
            raise TypeError("Целевой счет должен быть объектом BankAccount")
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма перевода должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        # Реализация метода (для прохождения теста)
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False


class SocialNetworkPost:
    """
    Класс, представляющий пост в социальной сети.

    Атрибуты:
    - author: str - автор поста
    - content: str - содержимое поста
    - likes: int - количество лайков
    """

    def __init__(self, author: str, content: str, likes: int = 0):
        """
        Создание и подготовка к работе объекта "Пост в социальной сети"

        :param author: Автор поста
        :param content: Текст поста
        :param likes: Начальное количество лайков

        Примеры:
        >>> post = SocialNetworkPost("user123", "Привет, мир!", 10)
        >>> post.author
        'user123'
        >>> post.content
        'Привет, мир!'
        """
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not author:
            raise ValueError("Автор не может быть пустой строкой")
        self.author = author

        if not isinstance(content, str):
            raise TypeError("Содержимое должно быть строкой")
        if not content:
            raise ValueError("Содержимое не может быть пустым")
        self.content = content

        if not isinstance(likes, int):
            raise TypeError("Количество лайков должно быть целым числом")
        if likes < 0:
            raise ValueError("Количество лайков не может быть отрицательным")
        self.likes = likes

    def add_like(self) -> None:
        """
        Добавление лайка к посту.

        Примеры:
        >>> post = SocialNetworkPost("user123", "Привет, мир!", 10)
        >>> post.add_like()
        >>> post.likes
        11
        """
        self.likes += 1

    def add_comment(self, commenter: str, comment: str) -> None:
        """
        Добавление комментария к посту.

        :param commenter: Автор комментария
        :param comment: Текст комментария

        :raise ValueError: Если комментарий пустой

        Примеры:
        >>> post = SocialNetworkPost("user123", "Привет, мир!", 10)
        >>> post.add_comment("user456", "Отличный пост!")
        """
        if not isinstance(commenter, str):
            raise TypeError("Автор комментария должен быть строкой")
        if not commenter:
            raise ValueError("Автор комментария не может быть пустой строкой")

        if not isinstance(comment, str):
            raise TypeError("Комментарий должен быть строкой")
        if not comment:
            raise ValueError("Комментарий не может быть пустым")
        # Реализация метода (для прохождения теста)
        pass


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name: str - имя студента
    - student_id: str - номер студенческого билета
    - grades: List[float] - список оценок
    """

    def __init__(self, name: str, student_id: str, grades: Optional[List[float]] = None):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: Имя студента
        :param student_id: Номер студенческого билета
        :param grades: Список оценок

        Примеры:
        >>> student = Student("Иван Иванов", "ST12345", [4.5, 5.0, 3.5])
        >>> student.name
        'Иван Иванов'
        >>> student.student_id
        'ST12345'
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name:
            raise ValueError("Имя не может быть пустой строкой")
        self.name = name

        if not isinstance(student_id, str):
            raise TypeError("Номер студенческого билета должен быть строкой")
        if not student_id:
            raise ValueError("Номер студенческого билета не может быть пустым")
        self.student_id = student_id

        if grades is None:
            grades = []

        if not isinstance(grades, list):
            raise TypeError("Оценки должны быть представлены списком")

        for grade in grades:
            if not isinstance(grade, (int, float)):
                raise TypeError("Каждая оценка должна быть числом")
            if grade < 0 or grade > 5:
                raise ValueError("Оценка должна быть в диапазоне от 0 до 5")

        self.grades = grades

    def add_grade(self, grade: float) -> None:
        """
        Добавление новой оценки.

        :param grade: Новая оценка

        :raise ValueError: Если оценка вне допустимого диапазона

        Примеры:
        >>> student = Student("Иван Иванов", "ST12345", [4.5, 5.0, 3.5])
        >>> student.add_grade(4.0)
        >>> len(student.grades)
        4
        """
        if not isinstance(grade, (int, float)):
            raise TypeError("Оценка должна быть числом")
        if grade < 0 or grade > 5:
            raise ValueError("Оценка должна быть в диапазоне от 0 до 5")
        # Реализация метода (для прохождения теста)
        self.grades.append(grade)

    def calculate_average_grade(self) -> float:
        """
        Расчет среднего балла студента.

        :return: Средний балл

        Примеры:
        >>> student = Student("Иван Иванов", "ST12345", [4.5, 5.0, 3.5])
        >>> round(student.calculate_average_grade(), 2)
        4.33
        """
        if not self.grades:
            return 0.0
        # Реализация метода (для прохождения теста)
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self, threshold: float = 4.5) -> bool:
        """
        Проверка, является ли студент отличником.

        :param threshold: Пороговое значение для отличника

        :return: True если средний балл выше порога, иначе False

        Примеры:
        >>> student = Student("Иван Иванов", "ST12345", [4.5, 5.0, 4.8])
        >>> student.is_excellent_student()
        True
        """
        if not isinstance(threshold, (int, float)):
            raise TypeError("Порог должен быть числом")
        if threshold < 0 or threshold > 5:
            raise ValueError("Порог должен быть в диапазоне от 0 до 5")
        # Реализация метода (для прохождения теста)
        return self.calculate_average_grade() >= threshold


if __name__ == "__main__":
    doctest.testmod(verbose=True)
