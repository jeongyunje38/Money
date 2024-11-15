from enum import Enum


class TradingAction(Enum):

    BUY = 1
    HOLD = 2
    SELL = 3


class StrengthLevel(Enum):

    VERY_WEAK = 1
    WEAK = 2
    MODERATE = 3
    STRONG = 4
    VERY_STRONG = 5


class PriorityLevel(Enum):

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4
