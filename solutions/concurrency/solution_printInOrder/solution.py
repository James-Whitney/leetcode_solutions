import threading

# Solution for https://leetcode.com/problems/print-in-order/


class Foo:
    def __init__(self):
        self.first_lock = threading.Semaphore(1)
        self.second_lock = threading.Semaphore(0)
        self.third_lock = threading.Semaphore(0)
        pass

    def first(self, printFirst: "Callable[[], None]") -> None:
        self.first_lock.acquire()
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_lock.release()

    def second(self, printSecond: "Callable[[], None]") -> None:
        self.second_lock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_lock.release()

    def third(self, printThird: "Callable[[], None]") -> None:
        self.third_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
