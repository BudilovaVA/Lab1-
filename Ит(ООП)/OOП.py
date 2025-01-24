# TODO Написать 3 класса с документацией и аннотацией типов

class Magazine:
    def __init__(self, color: str, pages: int):
        """
        Инициализация журнала.

        param color: цвет журнала.
        param pages: количество страниц.

        Example:
            color = "red"
            pages = 60
        """
        self.color = color
        self.pages = pages

    def read (self) -> None:
        """
        Симулирует чтение
        """
        ...

    def lable (self):
        """
        Поставить метку
        """
        ...


class Furniture:
    def __init__(self, material: str, weight: float):
        """
        Инициализирует объект мебели.

        :param material: материал мебели.
        :param weight: вес мебели.
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом")

        self.material = material
        self.weight = weight

    def assemble(self) -> None:
        """
        Метод сборки мебели
        """
        ...

    def move(self, distance: float) -> None:
        """
        Метод для перемещения мебели на заданное расстояние
        :param distance: Расстояние перемещения в метрах.

        Example:
            >>> class Chair(Furniture):
            ...     def __init__(self, material: str, weight: float):
            ...        super().__init__(material, weight)
            ...     def assemble(self) -> None:
            ...         print("Chair assembled")
            ...     def move(self, distance: float) -> None:
            ...         print(f"Chair moved {distance} meters")
            >>> chair = Chair("wood", 5.0)
            >>> chair.move(2.5)
            Стул перемещен на 2.5 м
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть числом")
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        ...

    def get_info(self) -> str:
        """
        Метод для получения информации о мебели.
        :return str: Строка, содержащая информацию о мебели.
        """
        ...


class Table:
    def __init__(self, material: str, size: float):
        """
        Инициализация экземпляра класса
        :param material: материал стола.
        :param size: размер стола.
        """
        self.material = material
        self.size = size
        self.norm_size()
    def norm_size(self, normal_size: float):
        if normal_size <= 0:
            raise ValueError ("Размер стола должен быть больше 0")


    def sit(self, people: int) -> None:
        """
        Садиться за стол
        :param people: количество человек
        """
        ...

    def clean(self) -> None:
        """
        Убирать стол
        """
        ...

    def resize(self, new_size: float) -> None:
        """
        Изменять размер стола
        :param new_size: новый размер стола
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
    pass
