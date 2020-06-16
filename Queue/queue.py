class Queue:
    def __init__(self):
        self._list = list()
        self._count = 0

    def enqueue(self, item):
        self._list.append(item)
        self._count += 1

    def dequeue(self):
        try:
            assert self._count > 0, "Queue is EMPTY !!!"
            self._count -= 1
            return self._list.pop(0)
        except AssertionError:
            print("[-] Queue is EMPTY !!!")

    def size(self):
        return self._count

    def peek(self):
        try:
            assert self._count > 0, "QUEUE IS EMPTY !!!"
            return self._list[0]
        except AssertionError:
            print("[-] QUEUE IS EMPTY !!!")

    def is_empty(self):
        return self._count < 1
