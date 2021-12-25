from Coordinate import Coordinate
from PixelPainter import *
from Player import Player
import time

tk = Tk(className=' PyTron - Created by Shubh Patel')

# constants
pixel_length = 10
canvas_width = 120
canvas_height = 60
last_update = time.time()
refresh_delay = 33

p1_color = 'Blue'
p2_color = 'Red'

# game objects
painter = PixelPainter(tk, pixel_length, canvas_width, canvas_height, 'black')
p1 = Player(Coordinate(3 * canvas_width / 4, canvas_height / 2), painter, p1_color, 0, 0, canvas_width - 1,
            canvas_height - 1)
p2 = Player(Coordinate(canvas_width / 4, canvas_height / 2), painter, p2_color, 0, 0, canvas_width - 1,
            canvas_height - 1)


# key listener
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


# bind key listener
tk.bind_all('<Key>', read_keys)


# game ending sequence
def game_over(winner):
    def freeze():
        p1.stop()
        p2.stop()

    def victory(winner):
        painter.clear()
        if winner == 'Nobody':
            painter.write('Tie!', 'white')
        elif winner == 'Player 1':
            painter.write('Blue wins!', p1_color)
        elif winner == 'Player 2':
            painter.write('Red wins!', p2_color)

    def reset():
        painter.clear()
        p1.reset()
        p2.reset()
        tk.update_idletasks()
        tk.update()

    freeze()
    tk.after(2000, victory(winner))
    tk.after(2000, reset)


# game's main loop
def update():
    if p1.dead() or p2.dead():
        p1.update()
        p2.update()

        if p1.dead() and p2.dead():
            game_over('Nobody')
        elif p1.dead():
            game_over('Player 2')
        elif p2.dead():
            game_over('Player 1')

    if p1.next_dir is not None and p2.next_dir is not None:
        p1.update()
        p2.update()

    tk.after(refresh_delay, update)


update()
tk.mainloop()
