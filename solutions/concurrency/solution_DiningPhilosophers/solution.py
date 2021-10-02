from threading import Lock
from typing import Callable

# Solution to https://leetcode.com/problems/the-dining-philosophers/
# lame solution, only one philosopher eats at a time.


class DiningPhilosophers:
    def __init__(self) -> None:
        # self.philosophers = range(5)
        self.eating = Lock()
        pass

    # call the functions directly to execute, for example, eat()
    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:

        with self.eating:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
