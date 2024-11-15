from queue import PriorityQueue
from trading.prioritized_signal import PrioritizedSignal


class TradingQueue:
    def __init__(self):
        self.queue = PriorityQueue()

    def __len__(self):
        return self.queue.qsize()

    def add_signal(self, signal, priority):
        self.queue.put(PrioritizedSignal(priority, signal))

    def get_next(self):
        if not self.queue.empty():
            return self.queue.get().signal
        return None

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()
