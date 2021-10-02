import threading

# Solution for https://leetcode.com/problems/print-foobar-alternately/


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = threading.Semaphore(value=1)
        self.bar_lock = threading.Semaphore(value=0)

    def foo(self, printFoo: "Callable[[], None]") -> None:

        for i in range(self.n):
            self.foo_lock.acquire()

            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()

            self.bar_lock.release()

    def bar(self, printBar: "Callable[[], None]") -> None:

        for i in range(self.n):
            self.bar_lock.acquire()

            # printBar() outputs "bar". Do not change or remove this line.
            printBar()

            self.foo_lock.release()
