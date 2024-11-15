import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from .signal import Signal
from dataclasses import dataclass, field
from functools import total_ordering


@dataclass(order=False)
@total_ordering
class PrioritizedSignal:

    priority: int
    signal: Signal = field(compare=False)

    def __lt__(self, other):

        if self.priority == other.priority:

            return self.signal.timing < other.signal.timing

        else:

            return self.priority < other.priority
