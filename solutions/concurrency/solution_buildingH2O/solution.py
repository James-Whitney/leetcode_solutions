from threading import Semaphore, Barrier
from typing import Callable


# Solution to https://leetcode.com/problems/building-h2o/
class H2O:
    def __init__(self):
        self.h_lock = Semaphore(2)
        self.o_lock = Semaphore(1)
        self.water_barrier = Barrier(3)
        pass

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        with self.h_lock:
            self.water_barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        with self.o_lock:
            self.water_barrier.wait()

            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()
