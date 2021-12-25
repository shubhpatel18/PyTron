from Coordinate import Coordinate
from PixelPainter import *
from Player import Player
import time

tk = Tk(className=' PyTron - Created by Shubh Patel')

pixel_length = 10
canvas_width = 120
canvas_height = 60
last_update = time.time()
refresh_delay = 1 / 30

painter = PixelPainter(tk, pixel_length, canvas_width, canvas_height, 'black')
p1 = Player(Coordinate(3*canvas_width/4, canvas_height/2), painter, 'blue', 0, 0, canvas_width - 1, canvas_height - 1)
p2 = Player(Coordinate(canvas_width/4, canvas_height/2), painter, 'red', 0, 0, canvas_width - 1, canvas_height - 1)


def read_keys(event):
    if event.keysym == 'Up':
        p1.turn('UP')
    elif event.keysym == 'Down':
        p1.turn('DOWN')
    elif event.keysym == 'Left':
        p1.turn('LEFT')
    elif event.keysym == 'Right':
        p1.turn('RIGHT')

    elif event.keysym == 'w':
        p2.turn('UP')
    elif event.keysym == 's':
        p2.turn('DOWN')
    elif event.keysym == 'a':
        p2.turn('LEFT')
    elif event.keysym == 'd':
        p2.turn('RIGHT')


tk.bind_all('<Key>', read_keys)

while True:
    current_time = time.time()
    if current_time - last_update < refresh_delay:
        continue
    last_update = current_time

    p1.update()
    p2.update()

    tk.update_idletasks()
    tk.update()
