class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if (n + self._size) > self._capacity:
            raise ValueError(f"There is no capacity for adding {n} cookies.")
        else:
            self._size += n

    def withdraw(self, n):
        if (self._size - n) < 0:
            raise ValueError(f"There is no capacity for withdrawing {n} cookies.")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new):
        if new < 0:
            raise ValueError("Capacity should be non negative number.")
        else:
            self._capacity = new

    @property
    def size(self):
        return self._size
