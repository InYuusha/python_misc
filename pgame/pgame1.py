import pygame as p

import sys

p.init()
fpsClock=p.time.Clock()
surface=p.display.set_mode((400,800))
back=p.Color(225,125,125)
font=p.font.Font('freesansbold.ttf',40)
text=font.render("Hello",True,(125,225,225))
textrect=text.get_rect()
textrect.topleft=(200,400)

while True:
    surface.fill(back)
    surface.blit(text,textrect)
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
    p.display.update()
    fpsClock.tick(10)
    
