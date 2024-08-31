import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="shoot the alien"

message=""
alien=Actor("alien")
def draw():
    screen.clear()
    screen.fill("blue")
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)
def place_alien():
    alien.x=randint(50,450)
    alien.y=randint(50,450)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good shot!"
        place_alien()
    else:
        message="You missed!"

place_alien()
pgzrun.go()
