from threading import Semaphore
from typing import Callable

# solution to https://leetcode.com/problems/fizz-buzz-multithreaded/


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.number_lock = Semaphore(1)
        self.fizz_lock = Semaphore(0)
        self.buzz_lock = Semaphore(0)
        self.fizzbuzz_lock = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: "Callable[[], None]") -> None:
        for _ in (i for i in range(3, self.n + 1, 3) if i % 5 != 0):
            self.fizz_lock.acquire()
            printFizz()
            self.number_lock.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        for _ in (i for i in range(5, self.n + 1, 5) if i % 3 != 0):
            self.buzz_lock.acquire()
            printBuzz()
            self.number_lock.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        for _ in range(15, self.n + 1, 15):
            self.fizzbuzz_lock.acquire()
            printFizzBuzz()
            self.number_lock.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: "Callable[[int], None]") -> None:
        for i in range(1, self.n + 1):
            self.number_lock.acquire()

            if i % 3 == 0:
                if i % 5 == 0:
                    self.fizzbuzz_lock.release()
                else:
                    self.fizz_lock.release()
            else:
                if i % 5 == 0:
                    self.buzz_lock.release()
                else:
                    printNumber(i)
                    self.number_lock.release()
