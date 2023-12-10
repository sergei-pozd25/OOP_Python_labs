import doctest

class Number:
    def __init__(self, value: int, idx: int):
        """
        Создание и подготовка к работе объекта Number
        :param value: значение
        :param idx: индекс (место)

        >>> x1 = Number(2, 0)
        """
        if not isinstance(idx, int):
            raise TypeError("idx must be int")
        if idx < 0:
            raise ValueError("idx must be >= 0")
        self._value = value
        self._idx = idx
        ...

    def replace(self, index: int) -> None:
        """
        Перемещает элемент на новое место
        :param index: новый индекс элемента
        >>> x1 = Number(2, 0)
        >>> x1.replace(2)
        """
        if not isinstance(index, int):
            raise TypeError("Must be int")
        if index < 0:
            raise ValueError("Must be >= 0")
        self._idx = index
        ...

    def increment(self) -> None:
        """
        Инкрементирование числа
        :return: возвращает увеличеное число
        >>> x1 = Number(2, 0)
        >>> x1.increment()
        """
        self._value += 1
        ...

    def decrement(self) -> None:
        """
        Декрементирование числа
        :return: возвращает уменьшенное число
        >>> x1 = Number(2, 0)
        >>> x1.decrement()
        """
        self._value -= 1
        ...

if __name__ == "__main__":
    doctest.testmod()