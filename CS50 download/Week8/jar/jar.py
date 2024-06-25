class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        if n < 0:
            raise ValueError("Deposit cannot be negative")
        elif n + self._size > self._capacity:
            raise ValueError("Won't fit in the jar!")
        self._size += n


    def withdraw(self, n):
        if n < 0:
            raise ValueError("Withdrawal cannot be negative")
        elif self._size - n < 0:
            raise ValueError("Not enough cookies in the jar!")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size
