# TODO Написать 3 класса с документацией и аннотацией типов

class People:
    def sleep(self, time: int) -> None:
        """
        Симулирует сон
        :param time: длительность сна в часах
        :return: None

        >>> p = People()
        >>> p.sleep(7)
        """
        ...

    def work(self, time: int) -> None:
        """
        Симулирует работу
        :param time: длительность работу в часах
        :return: None

        >>> p = People()
        >>> p.work(10)
        """
        ...

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    def side_length(self):
        return 3/14 * self.radius * 2
c = Circle(3)
c.area()

    def area(self):
        ...
    def side_length(self):
        ...



class Table(ABC):
    def __init__(self, material: str, size: float):
        self.material = material
        self.size = size

    def sit(self, people: int) -> None:
        """
        Садиться за стол
        :param people: количество человек
        :return: None
        """
        ...

    def clean(self) -> None:
        """
        Убирать стол
        :return: None
        """
        ...

    def resize(self, new_size: float) -> None:
        """
        Изменять размер стола
        :param new_size: новый размер стола
        :return: None
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
