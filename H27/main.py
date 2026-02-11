# перше завдання

class Integers:
    def __init__(self, start=1):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        v = self.current
        self.current += 1
        return v


class EvenNumbers:
    def __init__(self, it):
        self.it = it
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            v = next(self.it)
            if v % 2 == 0:
                return v


class Squares:
    def __init__(self, it):
        self.it = it
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.it) ** 2


squares = Squares(EvenNumbers(Integers()))

for _ in range(10):
    print(next(squares))


print()

# друге завдання

class FlatIterator:
    def __init__(self, nested_list):
        self.stack = [iter(nested_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
                if isinstance(item, list):
                    self.stack.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.stack.pop()
        raise StopIteration


nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]

flat = FlatIterator(nested)

for x in flat:
    print(x)
