# Leetcode 1115. Print FooBar Alternately

# Use two Semaphores. 
# The foo_gate semaphore starts with a value of 1 because we want foo to print first

from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_gate = Semaphore(1)
        self.bar_gate = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_gate.acquire()
            printFoo()
            self.bar_gate.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_gate.acquire()
            printBar()
            self.foo_gate.release()

Run = FooBar(10)