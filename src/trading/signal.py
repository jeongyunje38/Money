class Signal:

    def __init__(self, ticker, quantity, action, strength, timing, timestamp):

        self._ticker = ticker
        self._quantity = quantity
        self._action = action
        self._strength = strength
        self._timing = timing
        self._timestamp = timestamp

    @property
    def ticker(self):

        return self._ticker

    @property
    def quantity(self):

        return self._quantity

    @property
    def action(self):

        return self._action

    @property
    def strength(self):

        return self._strength

    @property
    def timing(self):

        return self._timing

    @property
    def timestamp(self):

        return self._timestamp

    def to_dict(self):

        return {
            "ticker": self._ticker,
            "action": self._action,
            "strength": self._strength,
            "timing": self._timing,
            "timestamp": self._timestamp,
        }
