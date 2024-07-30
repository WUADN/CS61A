def count(n):
    if n > 0:
        yield n
        for y in count(n - 1):
            yield y
    else:
        print("end")


class LettersWithYield:
    def __init__(self, start="a", end="e") -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        next_letter = self.start
        while next_letter < self.end:
            yield next_letter
            next_letter = chr(ord(next_letter) + 1)


def all_pairs(s):
    yield from ((item1, item2) for item1 in s for item2 in s)
