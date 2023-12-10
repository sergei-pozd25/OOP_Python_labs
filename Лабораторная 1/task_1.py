import doctest

class Laptop:
    def __init__(self, model: str, memory_vol: float, occuped_memory: float, ram: float):
        """Создание и подготовка к работе Laptop
        :param model: модель
        :param memory_vol: объем памяти
        :param occuped_memory: объем занятой памяти
        :param RAM: объем оперативной памяти"""

        self.model = model
        self.memory_vol = memory_vol
        self.occuped_memory = occuped_memory
        self.ram = ram

        if not isinstance(memory_vol, (float, int)):
            raise TypeError("Memory_vol must be float or int")
        self.memory_vol = memory_vol
        if not isinstance(occuped_memory, (float, int)):
            raise TypeError("Memory must be float or int")
        if occuped_memory < 0:
            raise ValueError("Memory must be >= 0")
        self.occuped_memory = occuped_memory
        ...

    def if_overflow(self) -> bool:
        """Проверка на полную заполненность памяти
        :return: заполнено ли полностью"""
        #laptop = Laptop("H", 512, 512, 8)
        ...

    def add_ram (self, ram_mem: float) -> None:
        """Добавление памяти
        :param ram_mem: добавляемый объем
        laptop = Laptop("H", 512, 512, 8)
        laptop.add_ram(140)"""
        laptop = Laptop("H", 512, 100, 8)
        if not isinstance(ram_mem, (float, int)):
            raise TypeError("Must be int or float")
        if ram_mem < 0:
            raise ValueError("Must be > 0")
        ...

    def clean_memory(self, memory: float) -> None:
        """
        очистка памяти
        :param memory: объем очищаемой памяти
        :raise ValueError: Если количество освобождаемой памяти больше занятой
        :return: Оставшийся занятый объем
        """
        ...

if __name__ == "__main__":
    doctest.testmod()
