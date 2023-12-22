from tkinter import Tk, Button, Entry, Label, Canvas, Frame

class RegistrationLoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Регистрация и Вход')
        self.root.geometry("350x250")

        self.label_frame = Frame(self.root)
        self.label_frame.pack(pady=20)

        self.window_width = 300
        self.window_height = 200
        self.center_window(self.root, self.window_width, self.window_height)

        self.label_username = Label(self.label_frame, text="Логин:", font=("Arial", 12))
        self.label_username.grid(row=0, column=0, padx=10, pady=5)

        self.entry_username = Entry(self.label_frame, font=("Arial", 12))
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = Label(self.label_frame, text="Пароль:", font=("Arial", 12))
        self.label_password.grid(row=1, column=0, padx=10, pady=5)

        self.entry_password = Entry(self.label_frame, show="*", font=("Arial", 12))
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.button_register = Button(self.root, text="Зарегистрироваться", command=self.register, font=("Arial", 12))
        self.button_register.pack(pady=10)

        self.button_login = Button(self.root, text="Войти", command=self.login, font=("Arial", 12))
        self.button_login.pack()
    "Регистрация и проверка"
    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username.strip() and password.strip():
            if not self.check_user_exists(username):
                with open("users.txt", "a") as file:
                    file.write(f"Логин: {username}, Пароль: {password}\n")
                messagebox.showinfo("Регистрация", "Регистрация прошла успешно. Пожалуйста, войдите.")
                self.clear_entries()
            else:
                messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует")
        else:
            messagebox.showerror("Ошибка", "Введите имя пользователя и пароль")

    "Логин и проверка в файле"
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()


        if self.check_user_credentials(username, password):
            self.root.destroy()
            self.open_main_window()
        else:
            messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль")
    "Проверка строк на наличие пользователя в базе"
    def check_user_credentials(self, username, password):
        with open("users.txt", "r") as file:
            for line in file:
                if f"Логин: {username}, Пароль: {password}" in line:
                    return True
        return False
    "Ценрализация"
    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    "Проверка логина в файле на повтор"
    def check_user_exists(self, username):
        with open("users.txt", "r") as file:
            for line in file:
                if f"Логин: {username}" in line:
                    return True
        return False
    def clear_entries(self):
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
    def open_main_window(self):
        main_window = Tk()
        main_window.title('Шашки')
        "Централизация"
        window_width = 675
        window_height = 675
        screen_width = main_window.winfo_screenwidth()
        screen_height = main_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        main_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        main_window.resizable(0, 0)
        "Создание холста"
        main_canvas = Canvas(main_window, width=CELL_SIZE * 9, height=CELL_SIZE * 9)
        main_canvas.pack()
        game = Game(main_canvas, 9, 9)
        main_canvas.bind("<Motion>", game.mouse_move)
        main_canvas.bind("<Button-1>", game.mouse_down)

        main_window.mainloop()
def main():
    root = Tk()
    registration_login_window = RegistrationLoginWindow(root)
    root.mainloop()
class Point:
    def __init__(self, x: int = -1, y: int = -1):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        if isinstance(other, Point):
            return (
                self.x == other.x and
                self.y == other.y
            )

        return NotImplemented
class Move:
    def __init__(self, from_x: int = -1, from_y: int = -1, to_x: int = -1, to_y: int = -1):
        self.__from_x = from_x
        self.__from_y = from_y
        self.__to_x = to_x
        self.__to_y = to_y

    @property
    def from_x(self):
        return self.__from_x

    @property
    def from_y(self):
        return self.__from_y

    @property
    def to_x(self):
        return self.__to_x

    @property
    def to_y(self):
        return self.__to_y

    def __str__(self):
        return f'{self.from_x}-{self.from_y} -> {self.to_x}-{self.to_y}'

    def __repr__(self):
        return f'{self.from_x}-{self.from_y} -> {self.to_x}-{self.to_y}'

    def __eq__(self, other):
        if isinstance(other, Move):
            return (
                    self.from_x == other.from_x and
                    self.from_y == other.from_y and
                    self.to_x == other.to_x and
                    self.to_y == other.to_y
            )

        return NotImplemented
from enum import Enum, auto
class SideType(Enum):
    WHITE = auto()
    BLACK = auto()

    def opposite(side):
        if (side == SideType.WHITE):
            return SideType.BLACK
        elif (side == SideType.BLACK):
            return SideType.WHITE
        else: raise ValueError()

class CheckerType(Enum):
    NONE = auto()
    WHITE_REGULAR = auto()
    BLACK_REGULAR = auto()
    WHITE_QUEEN = auto()
    BLACK_QUEEN = auto()
    WHITE_KING = auto()
    BLACK_KING = auto()


#Выбор стороны
PLAYER_SIDE = SideType.WHITE
# Размер поля
CELL_SIZE = 75
# Анимация
ANIMATION_SPEED = 7
MAX_PREDICTION_DEPTH = 3
BORDER_WIDTH = 1 * 2
# Цвета
FIELD_COLORS = ['#f2f1ed', '#0d0d0c']
HOVER_BORDER_COLOR = '#54b346'
SELECT_BORDER_COLOR = '#800000'
POSIBLE_MOVE_CIRCLE_COLOR = '#800000'
MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]
# [Обычная пешка, дамка,вождь]
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN, CheckerType.WHITE_KING]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN, CheckerType.BLACK_KING]
class Checker:
    def __init__(self, type: CheckerType = CheckerType.NONE):
        self.__type = type

    @property
    def type(self):
        return self.__type

    def change_type(self, type: CheckerType):
        "Изменение типа шашки"
        self.__type = type

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
from tkinter import Canvas, Event, messagebox
from PIL import Image, ImageTk
from random import choice
from pathlib import Path
from time import sleep
from math import inf
class Game:
    def __init__(self, canvas: Canvas, x_field_size: int, y_field_size: int):
        self.__canvas = canvas
        self.__field = Field(x_field_size, y_field_size)

        self.__player_turn = True

        self.__hovered_cell = Point()
        self.__selected_cell = Point()
        self.__animated_cell = Point()

        self.__initialization_images()

        self.__draw_field()

        # Если игрок играет за чёрных, то совершить ход противника
        if (PLAYER_SIDE == SideType.BLACK):
            self.__handle_enemy_turn()

    def __initialization_images(self):
        "Загрузка картинок"

        self.__images = {
            CheckerType.WHITE_REGULAR: ImageTk.PhotoImage(
                Image.open(Path('pngs', 'white-regular.png')).resize((CELL_SIZE, CELL_SIZE), Image.ANTIALIAS)),
            CheckerType.BLACK_REGULAR: ImageTk.PhotoImage(
                Image.open(Path('pngs', 'black-regular.png')).resize((CELL_SIZE, CELL_SIZE), Image.ANTIALIAS)),
            CheckerType.WHITE_QUEEN: ImageTk.PhotoImage(
                Image.open(Path('pngs', 'white-queen.png')).resize((CELL_SIZE, CELL_SIZE), Image.ANTIALIAS)),
            CheckerType.BLACK_QUEEN: ImageTk.PhotoImage(
                Image.open(Path('pngs', 'black-queen.png')).resize((CELL_SIZE, CELL_SIZE), Image.ANTIALIAS)),
            CheckerType.WHITE_KING: ImageTk.PhotoImage(
                Image.open(Path('pngs', 'white-king.png')).resize((CELL_SIZE, CELL_SIZE), Image.ANTIALIAS)),
            CheckerType.BLACK_KING: ImageTk.PhotoImage(
                Image.open(Path('pngs', 'black-king.png')).resize((CELL_SIZE, CELL_SIZE), Image.ANTIALIAS))
        }
    def __animate_move(self, move: Move):
        "Перемещение шашки(анимация)"
        self.__animated_cell = Point(move.from_x, move.from_y)
        self.__draw_field()

        animated_checker = self.__canvas.create_image(move.from_x * CELL_SIZE, move.from_y * CELL_SIZE,
                                                      image=self.__images.get(
                                                          self.__field.type_piece(move.from_x, move.from_y)),
                                                      anchor='nw', tag='animated_checker')

        dx = 1 if move.from_x < move.to_x else -1
        dy = 1 if move.from_y < move.to_y else -1

        # Анимация
        for distance in range(abs(move.from_x - move.to_x)):
            for _ in range(100 // ANIMATION_SPEED):
                self.__canvas.move(animated_checker, ANIMATION_SPEED / 100 * CELL_SIZE * dx,
                                   ANIMATION_SPEED / 100 * CELL_SIZE * dy)
                self.__canvas.update()
                sleep(0.01)

        self.__animated_cell = Point()

    def __draw_field(self):
        "Рисовка сетки и поля"
        self.__canvas.delete('all')
        self.__draw_field_grid()
        self.__draw_checkers()

    def __draw_field_grid(self):
        "Сетка поля"
        for y in range(self.__field.y_size):
            for x in range(self.__field.x_size):
                self.__canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, x * CELL_SIZE + CELL_SIZE,
                                               y * CELL_SIZE + CELL_SIZE, fill=FIELD_COLORS[(y + 1 + x) % 2], width=0,
                                               tag='boards')

                # Отрисовка рамок у необходимых клеток
                if (x == self.__selected_cell.x and y == self.__selected_cell.y):
                    self.__canvas.create_rectangle(x * CELL_SIZE + BORDER_WIDTH // 2, y * CELL_SIZE + BORDER_WIDTH // 2,
                                                   x * CELL_SIZE + CELL_SIZE - BORDER_WIDTH // 2,
                                                   y * CELL_SIZE + CELL_SIZE - BORDER_WIDTH // 2,
                                                   outline=SELECT_BORDER_COLOR, width=BORDER_WIDTH, tag='border')
                elif (x == self.__hovered_cell.x and y == self.__hovered_cell.y):
                    self.__canvas.create_rectangle(x * CELL_SIZE + BORDER_WIDTH // 2, y * CELL_SIZE + BORDER_WIDTH // 2,
                                                   x * CELL_SIZE + CELL_SIZE - BORDER_WIDTH // 2,
                                                   y * CELL_SIZE + CELL_SIZE - BORDER_WIDTH // 2,
                                                   outline=HOVER_BORDER_COLOR, width=BORDER_WIDTH, tag='border')

                # Отрисовка возможных точек перемещения, если есть выбранная ячейка
                if (self.__selected_cell):
                    player_moves_list = self.__get_moves_list(PLAYER_SIDE)
                    for move in player_moves_list:
                        if (self.__selected_cell.x == move.from_x and self.__selected_cell.y == move.from_y):
                            self.__canvas.create_oval(move.to_x * CELL_SIZE + CELL_SIZE / 3,
                                                      move.to_y * CELL_SIZE + CELL_SIZE / 3,
                                                      move.to_x * CELL_SIZE + (CELL_SIZE - CELL_SIZE / 3),
                                                      move.to_y * CELL_SIZE + (CELL_SIZE - CELL_SIZE / 3),
                                                      fill=POSIBLE_MOVE_CIRCLE_COLOR, width=0,
                                                      tag='posible_move_circle')

    def __draw_checkers(self):
        "Шашки"
        for y in range(self.__field.y_size):
            for x in range(self.__field.x_size):
                # Не отрисовывать пустые ячейки и анимируемую шашку
                if (self.__field.type_piece(x, y) != CheckerType.NONE and not (
                        x == self.__animated_cell.x and y == self.__animated_cell.y)):
                    self.__canvas.create_image(x * CELL_SIZE, y * CELL_SIZE,
                                               image=self.__images.get(self.__field.type_piece(x, y)), anchor='nw',
                                               tag='checkers')

    def mouse_move(self, event: Event):
        "Перемещение мышки"
        x, y = (event.x) // CELL_SIZE, (event.y) // CELL_SIZE
        if (x != self.__hovered_cell.x or y != self.__hovered_cell.y):
            self.__hovered_cell = Point(x, y)

            # Если ход игрока, то перерисовать
            if (self.__player_turn):
                self.__draw_field()

    def mouse_down(self, event: Event):
        "Нажатие мышки"
        if not (self.__player_turn): return

        x, y = (event.x) // CELL_SIZE, (event.y) // CELL_SIZE

        # Если точка не внутри поля
        if not (self.__field.is_within_in_field(x, y)): return

        if (PLAYER_SIDE == SideType.WHITE):
            player_checkers = WHITE_CHECKERS
        elif (PLAYER_SIDE == SideType.BLACK):
            player_checkers = BLACK_CHECKERS
        else:
            return

        # Если нажатие по шашке игрока, то выбрать её
        if (self.__field.type_piece(x, y) in player_checkers):
            self.__selected_cell = Point(x, y)
            self.__draw_field()
        elif (self.__player_turn):
            move = Move(self.__selected_cell.x, self.__selected_cell.y, x, y)

            # Если нажатие по ячейке, на которую можно походить
            if (move in self.__get_moves_list(PLAYER_SIDE)):
                self.__handle_player_turn(move)

                # Если не ход игрока, то ход противника
                if not (self.__player_turn):
                    self.__handle_enemy_turn()

    def __handle_move(self, move: Move, draw: bool = True) -> bool:
        "Совершение хода"
        if (draw): self.__animate_move(move)

        # Изменение типа шашки, если она дошла до края
        if (move.to_y == 0 and self.__field.type_piece(move.from_x, move.from_y) == CheckerType.WHITE_REGULAR):
            self.__field.at_coordinate(move.from_x, move.from_y).change_type(CheckerType.WHITE_QUEEN)
        elif (move.to_y == self.__field.y_size - 1 and self.__field.type_piece(move.from_x,
                                                                               move.from_y) == CheckerType.BLACK_REGULAR):
            self.__field.at_coordinate(move.from_x, move.from_y).change_type(CheckerType.BLACK_QUEEN)

        # Изменение позиции шашки
        self.__field.at_coordinate(move.to_x, move.to_y).change_type(self.__field.type_piece(move.from_x, move.from_y))
        self.__field.at_coordinate(move.from_x, move.from_y).change_type(CheckerType.NONE)


        dx = -1 if move.from_x < move.to_x else 1
        dy = -1 if move.from_y < move.to_y else 1

        # Удаление съеденных шашек
        has_killed_checker = False
        x, y = move.to_x, move.to_y
        while (x != move.from_x or y != move.from_y):
            x += dx
            y += dy
            if (self.__field.type_piece(x, y) != CheckerType.NONE):
                self.__field.at_coordinate(x, y).change_type(CheckerType.NONE)

                has_killed_checker = True

        if (draw): self.__draw_field()

        return has_killed_checker

    def __handle_player_turn(self, move: Move):
        "Обработка хода игрока"
        self.__player_turn = False

        # Была ли убита шашка
        has_killed_checker = self.__handle_move(move)

        required_moves_list = list(
            filter(lambda required_move: move.to_x == required_move.from_x and move.to_y == required_move.from_y,
                   self.__get_required_moves_list(PLAYER_SIDE)))

        # Если есть ещё ход этой же шашкой
        if (has_killed_checker and required_moves_list):
            self.__player_turn = True

        self.__selected_cell = Point()

    def __handle_enemy_turn(self):
        "Обработка хода противника (компьютера)"
        self.__player_turn = False

        optimal_moves_list = self.__predict_optimal_moves(SideType.opposite(PLAYER_SIDE))

        for move in optimal_moves_list:
            self.__handle_move(move)

        self.__player_turn = True

        self.__check_for_game_over()

    def __check_for_game_over(self):
        "Проверка на конец игры"
        game_over = False

        white_moves_list = self.__get_moves_list(SideType.WHITE)
        if not (white_moves_list):
            # Белые проиграли
            answer = messagebox.showinfo('Конец игры', 'Чёрные выиграли')
            game_over = True

        black_moves_list = self.__get_moves_list(SideType.BLACK)
        if not (black_moves_list):
            # Чёрные проиграли
            answer = messagebox.showinfo('Конец игры', 'Белые выиграли')
            game_over = True
        if self.__field.kingScore():
            if self.__field.flagWK:
                # Черные проиграли
                answer = messagebox.showinfo('Конец игры', 'Белые выиграли')
            else:
                # Белые проиграли
                answer = messagebox.showinfo('Конец игры', 'Чёрные выиграли')
            game_over = True

        if (game_over):
            # Новая игра
            self.__init__(self.__canvas, self.__field.x_size, self.__field.y_size)

    def __predict_optimal_moves(self, side: SideType) -> list[Move]:
        "Предскать оптимальный ход"
        best_result = 0
        optimal_moves = []
        predicted_moves_list = self.__get_predicted_moves_list(side)

        if (predicted_moves_list):
            field_copy = Field.copy(self.__field)
            for moves in predicted_moves_list:
                for move in moves:
                    self.__handle_move(move, draw=False)

                try:
                    if (side == SideType.WHITE):
                        result = self.__field.white_score / self.__field.black_score
                    elif (side == SideType.BLACK):
                        result = self.__field.black_score / self.__field.white_score
                except ZeroDivisionError:
                    result = inf

                if (result > best_result):
                    best_result = result
                    optimal_moves.clear()
                    optimal_moves.append(moves)
                elif (result == best_result):
                    optimal_moves.append(moves)

                self.__field = Field.copy(field_copy)

        optimal_move = []
        if (optimal_moves):
            # Фильтрация хода
            for move in choice(optimal_moves):
                if (side == SideType.WHITE and self.__field.type_piece(move.from_x, move.from_y) in BLACK_CHECKERS):
                    break
                elif (side == SideType.BLACK and self.__field.type_piece(move.from_x, move.from_y) in WHITE_CHECKERS):
                    break

                optimal_move.append(move)

        return optimal_move

    def __get_predicted_moves_list(self, side: SideType, current_prediction_depth: int = 0,
                                   all_moves_list: list[Move] = [], current_moves_list: list[Move] = [],
                                   required_moves_list: list[Move] = []) -> list[Move]:
        "Предсказать все возможные ходы"

        if (current_moves_list):
            all_moves_list.append(current_moves_list)
        else:
            all_moves_list.clear()

        if (required_moves_list):
            moves_list = required_moves_list
        else:
            moves_list = self.__get_moves_list(side)

        if (moves_list and current_prediction_depth < MAX_PREDICTION_DEPTH):
            field_copy = Field.copy(self.__field)
            for move in moves_list:
                has_killed_checker = self.__handle_move(move, draw=False)

                required_moves_list = list(filter(
                    lambda required_move: move.to_x == required_move.from_x and move.to_y == required_move.from_y,
                    self.__get_required_moves_list(side)))

                # Если есть ещё ход этой же шашкой
                if (has_killed_checker and required_moves_list):
                    self.__get_predicted_moves_list(side, current_prediction_depth, all_moves_list,
                                                    current_moves_list + [move], required_moves_list)
                else:
                    self.__get_predicted_moves_list(SideType.opposite(side), current_prediction_depth + 1,
                                                    all_moves_list, current_moves_list + [move])

                self.__field = Field.copy(field_copy)

        return all_moves_list

    def __get_moves_list(self, side: SideType) -> list[Move]:
        "Список ходов"
        moves_list = self.__get_required_moves_list(side)
        if not (moves_list):
            moves_list = self.__get_optional_moves_list(side)
        return moves_list

    def __get_required_moves_list(self, side: SideType) -> list[Move]:
        "Обязательные ходы"
        moves_list = []

        # Определение типов шашек
        if (side == SideType.WHITE):
            friendly_checkers = WHITE_CHECKERS
            enemy_checkers = BLACK_CHECKERS

        elif (side == SideType.BLACK):
            friendly_checkers = BLACK_CHECKERS
            enemy_checkers = WHITE_CHECKERS

        else:
            return moves_list

        for y in range(self.__field.y_size):
            for x in range(self.__field.x_size):

                # Для обычной шашки
                if (self.__field.type_piece(x, y) == friendly_checkers[0]):
                    for offset in MOVE_OFFSETS:
                        if not (self.__field.is_within_in_field(x + offset.x * 2, y + offset.y * 2)): continue

                        if self.__field.type_piece(x + offset.x,
                                                   y + offset.y) in enemy_checkers and self.__field.type_piece(
                                x + offset.x * 2, y + offset.y * 2) == CheckerType.NONE:
                            moves_list.append(Move(x, y, x + offset.x * 2, y + offset.y * 2))
                # Для вождя
                elif (self.__field.type_piece(x, y) == friendly_checkers[2]):
                    for offset in MOVE_OFFSETS:
                        if not (self.__field.is_within_in_field(x + offset.x * 2, y + offset.y * 2)): continue

                        if self.__field.type_piece(x + offset.x,
                                                   y + offset.y) in enemy_checkers and self.__field.type_piece(
                                x + offset.x * 2, y + offset.y * 2) == CheckerType.NONE:
                            moves_list.append(Move(x, y, x + offset.x * 2, y + offset.y * 2))
                # Для дамки
                elif (self.__field.type_piece(x, y) == friendly_checkers[1]):
                    for offset in MOVE_OFFSETS:
                        if not (self.__field.is_within_in_field(x + offset.x * 2, y + offset.y * 2)): continue

                        has_enemy_checker_on_way = False

                        for shift in range(1, self.__field.size):
                            if not (
                            self.__field.is_within_in_field(x + offset.x * shift, y + offset.y * shift)): continue

                            # Если на пути не было вражеской шашки
                            if (not has_enemy_checker_on_way):
                                if (self.__field.type_piece(x + offset.x * shift,
                                                            y + offset.y * shift) in enemy_checkers):
                                    has_enemy_checker_on_way = True
                                    continue
                                # Если на пути союзная шашка - то закончить цикл
                                elif (self.__field.type_piece(x + offset.x * shift,
                                                              y + offset.y * shift) in friendly_checkers):
                                    break

                            # Если на пути была вражеская шашка
                            if (has_enemy_checker_on_way):
                                if (self.__field.type_piece(x + offset.x * shift,
                                                            y + offset.y * shift) == CheckerType.NONE):
                                    moves_list.append(Move(x, y, x + offset.x * shift, y + offset.y * shift))
                                else:
                                    break

        return moves_list

    def __get_optional_moves_list(self, side: SideType) -> list[Move]:
        "Необязательные ходы"
        moves_list = []

        # Определение типов шашек
        if (side == SideType.WHITE):
            friendly_checkers = WHITE_CHECKERS
        elif (side == SideType.BLACK):
            friendly_checkers = BLACK_CHECKERS
        else:
            return moves_list

        for y in range(self.__field.y_size):
            for x in range(self.__field.x_size):
                # Для обычной шашки
                if (self.__field.type_piece(x, y) == friendly_checkers[0]):
                    for offset in MOVE_OFFSETS[:2] if side == SideType.WHITE else MOVE_OFFSETS[2:]:
                        if not (self.__field.is_within_in_field(x + offset.x, y + offset.y)): continue

                        if (self.__field.type_piece(x + offset.x, y + offset.y) == CheckerType.NONE):
                            moves_list.append(Move(x, y, x + offset.x, y + offset.y))

                # Для вождя
                elif (self.__field.type_piece(x, y) == friendly_checkers[2]):
                    for offset in MOVE_OFFSETS[:2] if side == SideType.WHITE else MOVE_OFFSETS[2:]:
                        if not (self.__field.is_within_in_field(x + offset.x, y + offset.y)): continue

                        if (self.__field.type_piece(x + offset.x, y + offset.y) == CheckerType.NONE):
                            moves_list.append(Move(x, y, x + offset.x, y + offset.y))

                # Для дамки
                elif (self.__field.type_piece(x, y) == friendly_checkers[1]):
                    for offset in MOVE_OFFSETS:
                        if not (self.__field.is_within_in_field(x + offset.x, y + offset.y)): continue

                        for shift in range(1, self.__field.size):
                            if not (
                            self.__field.is_within_in_field(x + offset.x * shift, y + offset.y * shift)): continue

                            if (self.__field.type_piece(x + offset.x * shift,
                                                        y + offset.y * shift) == CheckerType.NONE):
                                moves_list.append(Move(x, y, x + offset.x * shift, y + offset.y * shift))
                            else:
                                break
        return moves_list
if __name__ == '__main__':
    main()
