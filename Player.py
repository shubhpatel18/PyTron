class Player:
    def __init__(self, coord, painter, color, x_min, y_min, x_max, y_max):
        self.coord = coord
        self.painter = painter
        self.color = color
        self.dir = None
        self.next_dir = None
        self.alive = True

        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

        painter.paint(self.coord, color)

    def turn(self, new_dir):
        if not (
                (self.dir == 'UP' and new_dir == 'DOWN') or
                (self.dir == 'DOWN' and new_dir == 'UP') or
                (self.dir == 'LEFT' and new_dir == 'RIGHT') or
                (self.dir == 'RIGHT' and new_dir == 'LEFT')
        ):
            self.next_dir = new_dir

    def is_invalid(self, coord):
        return not ((self.x_min <= coord.x <= self.x_max) and (self.y_min <= coord.y <= self.y_max))

    def update(self):
        if not self.alive:
            return

        self.dir = self.next_dir
        if self.dir is None:
            return
        elif self.dir == 'UP':
            self.coord = self.coord.get_above()
        elif self.dir == 'DOWN':
            self.coord = self.coord.get_below()
        elif self.dir == 'LEFT':
            self.coord = self.coord.get_left()
        elif self.dir == 'RIGHT':
            self.coord = self.coord.get_right()

        if self.is_invalid(self.coord):
            self.alive = False
            return

        self.painter.paint(self.coord, self.color)
