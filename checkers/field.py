from checkers.enums import CheckerType
from checkers.checker import Checker
from checkers.constants import WHITE_CHECKERS, BLACK_CHECKERS
from checkers.point import Point

from functools import reduce


class Field:
    def __init__(self, x_size: int, y_size: int):
        self.flagWK = False
        self.flagBK = False
        self.__x_size = x_size
        self.__y_size = y_size
        self.__generate()

    @property
    def x_size(self) -> int:
        return self.__x_size

    @property
    def y_size(self) -> int:
        return self.__y_size

    @property
    def size(self) -> int:
        return max(self.x_size, self.y_size)

    @classmethod
    def copy(cls, field_instance):
        "Копия поля"
        field_copy = cls(field_instance.x_size, field_instance.y_size)

        for y in range(field_instance.y_size):
            for x in range(field_instance.x_size):
                field_copy.at_coordinate(x, y).change_type(field_instance.type_piece(x, y))

        return field_copy

    def __generate(self):
        "Генерация поля с шашками"
        self.__checkers = [[Checker() for x in range(self.x_size)] for y in range(self.y_size)]

        for y in range(self.y_size):
            for x in range(self.x_size):
                if not ((y + x) % 2):
                    if (y < 3):
                        self.__checkers[y][x].change_type(CheckerType.BLACK_REGULAR)
                        if x == 4 and y == 0:
                            self.__checkers[y][x].change_type(CheckerType.BLACK_KING)
                    elif (y >= self.y_size - 3):
                        self.__checkers[y][x].change_type(CheckerType.WHITE_REGULAR)
                        if x == 4 and y == 8:
                            self.__checkers[y][x].change_type(CheckerType.WHITE_KING)

    def type_piece(self, x: int, y: int) -> CheckerType:
        "Тип шашки по координатам"
        return self.__checkers[y][x].type

    def kingScore(self):
        "Убийство Вождя"
        for y in range(self.y_size):
            for x in range(self.x_size):
                if self.type_piece(x, y) == CheckerType.WHITE_KING:
                    self.flagWK = True
                if self.type_piece(x, y) == CheckerType.BLACK_KING:
                    self.flagBK = True
        if self.flagBK and self.flagWK:
            return False
        else:
            return True

    def at_coordinate(self, x: int, y: int) -> Checker:
        "Получение шашки по координатам"
        return self.__checkers[y][x]

    def is_within_in_field(self, x: int, y: int) -> bool:
        "В пределах поля или нет"
        return (0 <= x < self.x_size and 0 <= y < self.y_size)

    @property
    def white_checkers_count(self) -> int:
        "Кол-во белых шашек на поле"
        return sum(reduce(lambda acc, checker: acc + (checker.type in WHITE_CHECKERS), checkers, 0) for checkers in
                   self.__checkers)

    @property
    def black_checkers_count(self) -> int:
        "Кол-во чёрных шашек на поле"
        return sum(reduce(lambda acc, checker: acc + (checker.type in BLACK_CHECKERS), checkers, 0) for checkers in
                   self.__checkers)

    @property
    def white_score(self) -> int:
        "Счёт белых"
        return sum(reduce(lambda acc, checker: acc + (checker.type == CheckerType.WHITE_REGULAR) + (
                    checker.type == CheckerType.WHITE_QUEEN) * 3 + (checker.type == CheckerType.WHITE_KING) * 100,
                          checkers, 0) for checkers in self.__checkers)

    @property
    def black_score(self) -> int:
        "Счёт черных"
        return sum(reduce(lambda acc, checker: acc + (checker.type == CheckerType.BLACK_REGULAR) + (
                    checker.type == CheckerType.BLACK_QUEEN) * 3 + (checker.type == CheckerType.BLACK_KING) * 100,
                          checkers, 0) for checkers in self.__checkers)