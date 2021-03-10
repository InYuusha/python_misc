import pygame as p
from pygame.locals import *
import sys

chkerr=p.init()
print(chkerr)
fps=p.time.Clock()
game_window=p.display.set_mode((600,800))
p.display.set_caption("My Game")

back=p.Color(225,0,0)
font=p.font.SysFont("aerial",90)
text=font.render("My Game",True,(0,225,225))
text_rect=text.get_rect()
rct=p.Rect(300,300,400,500)
print(rct)

print(text_rect)
while True:
    
    game_window.fill(back)
    game_window.blit(text,text_rect)
    p.draw.rect(game_window,[255,0,125],[200,200,100,100],1)
    for event in p.event.get():
        if event.type==QUIT:
            p.quit()
            sys.exit()

    p.display.update()
    fps.tick(10)

            
    
