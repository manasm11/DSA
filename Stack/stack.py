class Stack:
    def __init__(self):
        self._list = list()
        self._count = 0

    def push(self, item):
        self._list.append(item)
        self._count += 1

    def pop(self):
        assert self._count > 0, "Stack is empty."
        self._count -= 1
        return self._list.pop()

    def peek(self):
        assert self._count > 0, "Stack is empty."
        return self._list[-1]

    def is_empty(self):
        return self._count < 1

    def size(self):
        return self._count
