import pygame as p
import sys
import random as r
p.init()
screen=p.display.set_mode((600,700))

def create(x,y):
     red=(255,0,0)
    
     obj=p.draw.polygon(screen,red,[(x,150),(200,250),(300,y)])
     return obj
while True:
    x=r.randrange(0,500)
    y=r.randrange(200,500)
    
   
    
    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
    if p.mouse.get_pressed()[0]:
         obj=create(x,y)
        
        
    p.display.update()
    
            
