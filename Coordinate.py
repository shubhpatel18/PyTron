class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_above(self):
        return Coordinate(self.x, self.y - 1)

    def get_below(self):
        return Coordinate(self.x, self.y + 1)

    def get_left(self):
        return Coordinate(self.x - 1, self.y)

    def get_right(self):
        return Coordinate(self.x + 1, self.y)
