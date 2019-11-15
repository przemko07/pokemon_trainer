class Parser:
    def __init__(self, args):
        self.args = args
        self.index = 0

    def peek():
        return peek_index(0)

    def peek_index(self, i):
        if (self.index + i >= len(self.args)):
            return None
        return self.args[self.index + i]

    def move(self, i):
        index += i

