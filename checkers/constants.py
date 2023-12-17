from checkers.point import Point
from checkers.enums import CheckerType, SideType

# Сторона за которую играет игрок
PLAYER_SIDE = SideType.WHITE

# Размер поля
X_SIZE = Y_SIZE = 9
# Размер ячейки (в пикселях)
CELL_SIZE = 75

# Скорость анимации (больше = быстрее)
ANIMATION_SPEED = 7
MAX_PREDICTION_DEPTH = 3

# Ширина рамки (Желательно должна быть чётной)
BORDER_WIDTH = 1 * 2

# Цвета игровой доски
FIELD_COLORS = ['#f2f1ed', '#0d0d0c']
# Цвет рамки при наведении на ячейку мышкой
HOVER_BORDER_COLOR = '#54b346'
# Цвет рамки при выделении ячейки
SELECT_BORDER_COLOR = '#800000'
# Цвет кружков возможных ходов
POSIBLE_MOVE_CIRCLE_COLOR = '#800000'

MOVE_OFFSETS = [
    Point(-1, -1),
    Point( 1, -1),
    Point(-1,  1),
    Point( 1,  1)
]

# Массивы типов белых и чёрных шашек [Обычная пешка, дамка]
WHITE_CHECKERS = [CheckerType.WHITE_REGULAR, CheckerType.WHITE_QUEEN, CheckerType.WHITE_KING]
BLACK_CHECKERS = [CheckerType.BLACK_REGULAR, CheckerType.BLACK_QUEEN, CheckerType.BLACK_KING]