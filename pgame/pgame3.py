import pygame as p
from pygame.locals import*
import sys

p.init()
back=p.display.set_mode((800,600))
fps=p.time.Clock()
class square():
    def __init__(self,x,y,color,size):
        self.x=x
        self.y=y
        self.color=color
        self.size=size
    def drawit(self):
        p.draw.rect(back,self.color,(self.x,self.y,self.size,self.size),1)


class blocks:

    def __init__(self):
        self.blocks=[]
        for i in range(60,180,30):
            self.blocks.append(square(200,300,(225,0,0),i))
            
    def draw(self):
        for i  in range(4):
           
            self.blocks[i].drawit()
while True:
    back.fill((0,225,0))
    blc=blocks()
    
    blc.draw()
    
    for event in p.event.get():
        if event.type==QUIT:
            p.quit()
            sys.exit()
                               
    p.display.update()
    fps.tick(10)
