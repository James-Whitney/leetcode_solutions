from threading import Semaphore
from typing import Callable

# Solution for https://leetcode.com/problems/print-zero-even-odd/


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.zero_lock = Semaphore(1)
        self.even_lock = Semaphore(0)
        self.odd_lock = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()

            printNumber(0)

            if i % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()

            printNumber(i)

            self.zero_lock.release()

    def odd(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()

            printNumber(i)

            self.zero_lock.release()
