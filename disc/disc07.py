def draw(hand, positions):
    """Remove and return the items at positions from hand.
    >>> hand = ['A', 'K', 'Q', 'J', 10, 9]
    >>> draw(hand, [2, 1, 4])
    ['K', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """
    return list(reversed([hand.pop(i) for i in reversed(sorted(positions))]))


LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"


class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1


class Button:
    """A button on a keyboard.
    >>> f = lambda c: print(c, end='') # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """

    caps_lock = CapsLock()

    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        """Call output on letter (maybe uppercased), then return the button that was
        pressed."""
        self.pressed += 1
        is_odd = Button.caps_lock.pressed % 2 == 1
        if is_odd:
            self.output(self.letter.upper())

        else:
            self.output(self.letter)
        return self


class Keyboard:
    """A keyboard.
    >>> Button.caps_lock.pressed = 0 # Reset the caps_lock key
    >>> bored = Keyboard()
    """

    def __init__(self):
        self.keys = {c: Button(c, ...) for c in LOWERCASE_LETTERS}


if __name__ == "__main__":
    f = lambda c: print(c, end="")
    k, e, y = Button("k", f), Button("e", f), Button("y", f)
    e.press().p
