"""
Модуль, демонстрирующий наследование на примере иерархии транспортных средств.
"""


class Vehicle:
    """Базовый класс, представляющий общее транспортное средство.

    Атрибуты:
        make (str): Производитель.
        model (str): Модель.
        year (int): Год выпуска.
        _mileage (float): Пробег в километрах. Защищённый атрибут,
            чтобы предотвратить прямое изменение извне; используйте методы
            `drive()` и `get_mileage()`.
    """

    def __init__(self, make: str, model: str, year: int, mileage: float = 0.0) -> None:
        """Инициализировать транспортное средство.

        Аргументы:
            make: Производитель.
            model: Модель.
            year: Год выпуска.
            mileage: Начальный пробег (по умолчанию 0.0).
        """
        self.make = make
        self.model = model
        self.year = year
        self._mileage = mileage  # непубличный, внутреннее состояние

    def __str__(self) -> str:
        """Вернуть удобное для пользователя строковое представление."""
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """Вернуть подробное строковое представление для разработчиков."""
        return (
            f"{self.__class__.__name__}(make='{self.make}', model='{self.model}', "
            f"year={self.year}, mileage={self._mileage})"
        )

    def drive(self, distance: float) -> None:
        """Проехать заданное расстояние, увеличивая пробег.

        Аргументы:
            distance: Расстояние в километрах (должно быть неотрицательным).

        Исключения:
            ValueError: Если расстояние отрицательное.
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self._mileage += distance

    def get_mileage(self) -> float:
        """Вернуть текущий пробег."""
        return self._mileage


class Car(Vehicle):
    """Дочерний класс, представляющий легковой автомобиль.

    Расширяет базовый класс количеством дверей и переопределяет метод drive
    для имитации расхода топлива.

    Атрибуты:
        num_doors (int): Количество дверей (например, 2, 4).
    """

    def __init__(
        self, make: str, model: str, year: int, num_doors: int, mileage: float = 0.0
    ) -> None:
        """Инициализировать легковой автомобиль.

        Аргументы:
            make: Производитель.
            model: Модель.
            year: Год выпуска.
            num_doors: Количество дверей.
            mileage: Начальный пробег (по умолчанию 0.0).
        """
        # Расширяем конструктор базового класса
        super().__init__(make, model, year, mileage)
        self.num_doors = num_doors

    def __str__(self) -> str:
        """Вернуть удобное строковое представление с количеством дверей."""
        return f"{super().__str__()} (Дверей: {self.num_doors})"

    def __repr__(self) -> str:
        """Вернуть подробное представление для разработчиков, включая двери."""
        return (
            f"{self.__class__.__name__}(make='{self.make}', model='{self.model}', "
            f"year={self.year}, num_doors={self.num_doors}, mileage={self._mileage})"
        )

    def drive(self, distance: float) -> None:
        """Проехать расстояние, обновить пробег и имитировать расход топлива.

        Аргументы:
            distance: Расстояние в километрах.
        """
        # Наследуем базовую логику обновления пробега
        super().drive(distance)
        # Поведение, специфичное для легкового автомобиля
        print(f"Автомобиль проехал {distance} км. Расход топлива симулирован.")


if __name__ == "__main__":
    # Простая демонстрация
    vehicle = Vehicle("Generic", "V1", 2020, 100.0)
    print(vehicle)
    vehicle.drive(50.0)
    print(f"Пробег: {vehicle.get_mileage()} км")

    car = Car("Toyota", "Corolla", 2022, 4, 5000.0)
    print(car)
    car.drive(150.0)
    print(f"Пробег: {car.get_mileage()} км")
