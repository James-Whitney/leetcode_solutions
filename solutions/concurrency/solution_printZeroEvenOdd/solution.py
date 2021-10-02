from threading import Semaphore
from typing import Callable

# Solution for https://leetcode.com/problems/building-h2o/


class H2O:
    def __init__(self):
        pass

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
