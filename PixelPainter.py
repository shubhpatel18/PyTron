from tkinter import *


class PixelPainter:
    def __init__(self, tk, pixel_length, canvas_width, canvas_height, bg_color):
        self.pixel_length = pixel_length
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.occupied = [[False for _ in range(canvas_height)] for _ in range(canvas_width)]

        self.c = Canvas(tk, width=canvas_width * pixel_length, height=canvas_height * pixel_length, bg=bg_color)
        self.c.pack()
        tk.resizable(0, 0)

    def paint(self, coord, color):
        self.c.create_rectangle(coord.x * self.pixel_length, coord.y * self.pixel_length,
                                (coord.x + 1) * self.pixel_length - 1, (coord.y + 1) * self.pixel_length - 1,
                                outline=color, fill=color)
        self.occupied[int(coord.x)][int(coord.y)] = True

    def is_occupied(self, coord):
        return self.occupied[int(coord.x)][int(coord.y)]
