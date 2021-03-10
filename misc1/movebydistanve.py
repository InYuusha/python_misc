import pygame as p
import sys

p.init()
back=p.display.set_mode((700,800))
fps=p.time.Clock()
speed=2
x_pos=50
y_pos=50
while True:
    back.fill((0,0,255))
    p.draw.rect(back,(0,255,0),[x_pos,y_pos,80,80])
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
   
   # keys=p.key.get_pressed()
    #if keys==p.K_RIGHT:    
   
    
   
    x_pos+=speed
    y_pos+=speed
            
    p.display.update()
    fps.tick(70)
    
    
    
