from checkers.point import Point
from checkers.enums import CheckerType, SideType

#Выбор стороны
PLAYER_SIDE = SideType.WHITE

# Размер поля
X_SIZE = Y_SIZE = 9
CELL_SIZE = 75

# Скорость анимации (больше = быстрее)
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