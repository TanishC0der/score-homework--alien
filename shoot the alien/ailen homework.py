import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="shoot the alien"
message=""
score=0
high_score=0

alien=Actor("alien")


#creating alien and background
def draw():
    screen.clear()
    screen.fill(" light blue")
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)
    screen.draw.text("Score: :"+str(score),color="Black",center=(100,10))
    screen.draw.text("High score:"+str(high_score),color="Black", center=(200,10))
    
        
def place_alien():
    alien.x=randint(50,450)
    alien.y=randint(50,450)

#when mouse collides with the alien
def on_mouse_down(pos):
    global message
    global score
    global high_score
    if alien.collidepoint(pos):
        message="Good shot!"
        score=score+1
        if score>high_score:
            high_score=score
        place_alien()
    else:
        message="You missed!"
        score=score-1




        


    


place_alien()
pgzrun.go()