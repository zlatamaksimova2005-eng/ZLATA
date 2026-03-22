class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages  # Используем сеттер для установки значения

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("pages must be an integer")
        if value <= 0:
            raise ValueError("pages must be positive")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Страниц: {self.pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration  # Используем сеттер для установки значения

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("duration must be a number")
        if value <= 0:
            raise ValueError("duration must be positive")
        self._duration = float(value)

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


# Проверка работы классов
if __name__ == "__main__":
    # Создаем экземпляры
    paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
    audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

    print(paper_book)
    print(repr(paper_book))

    print(audio_book)
    print(repr(audio_book))

    # Проверка свойств
    try:
        paper_book.name = "Новое название"  # Должно вызвать ошибку
    except AttributeError as e:
        print(f"Ошибка при попытке изменить название: {e}")

    try:
        paper_book.pages = -100  # Должно вызвать ошибку
    except ValueError as e:
        print(f"Ошибка при установке pages: {e}")

    try:
        paper_book.pages = "сто"  # Должно вызвать ошибку
    except TypeError as e:
        print(f"Ошибка при установке pages: {e}")

    # Проверка наследования
    print(f"\npaper_book является экземпляром Book: {isinstance(paper_book, Book)}")
    print(f"paper_book является экземпляром PaperBook: {isinstance(paper_book, PaperBook)}")
    print(f"audio_book является экземпляром Book: {isinstance(audio_book, Book)}")
    print(f"audio_book является экземпляром AudioBook: {isinstance(audio_book, AudioBook)}")
