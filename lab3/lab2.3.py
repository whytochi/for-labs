class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        """Возвращает название книги (только для чтения)."""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги (только для чтения)."""
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги с количеством страниц."""

    def __init__(self, name: str, author: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        """Возвращает количество страниц (только для чтения)."""
        return self._pages

    def __str__(self):
        return super().__str__() + f", количество страниц {self.pages}"


class AudioBook(Book):
    """Класс аудиокниги с продолжительностью."""

    def __init__(self, name: str, author: str, duration: float):
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность должна быть числом")
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        """Возвращает длительность аудиокниги (только для чтения)."""
        return self._duration

    def __str__(self):
        return super().__str__() + f", длительность {self.duration}"


# Проверка работы кода
a = PaperBook("generation п", "Пелевин", 500)
print(a)