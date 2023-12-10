import doctest

class Matrix:
    def __init__(self, cols: int, rows: int):
        """
        Создание и подготовка к работе объекта Матрица
        :param cols: число столбцов
        :param rows: число строк

        >>> matrix = Matrix(4, 4) # инициализация элемента класса
        """
        if not isinstance(cols ,int):
            raise TypeError("Not int")
        if cols < 0:
            raise ValueError("< 0")
        if not isinstance(rows, int):
            raise TypeError("Not int")
        if rows < 0:
            raise ValueError("< 0")
        self.rows = rows
        self.cols = cols
        ...

    def create_zero_matrix(self) -> None:
        """
        Создание нулевой матрицы
        :return: Возвращает нулевую матрицу заданного размера

        >>> matrix = Matrix(3, 3)
        >>> matrix.create_zero_matrix()
        """
        ...

    def set_random(self, range: int) -> None:
        """
        Заполнение матрицы рандомными значениями
        :param range: Диапазон значений
        :return: Заполненная матрица
        >>> matrix = Matrix(3, 3)
        >>> matrix.set_random(10) # заполнение значениями в указаном диапазоне
        """
        if range < 0:
            raise ValueError("range < 0")
        ...

    def transposition(self) -> None:
        """
        Транспонирование матрицы
        :return: Возврат транспонированной матрицы
        >>> matrix = Matrix(3, 3)
        >>> matrix.transposition()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()