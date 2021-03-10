import pygame as p
import random as r,sys
p.init()
back=p.display.set_mode((600,700))
while True:
     circle=p.draw.circle(back,(200,200,200),(200,100),50,0)
     p.draw.circle(back,(255,255,255),(180,90),25)
     rgb=(r.randrange(0,255),r.randrange(0,255),r.randrange(0,255))
    # x=r.randrange(50,500)
     #y=r.randrange(50,650)
     for event in p.event.get():
         if event.type==p.QUIT:
             p.quit()
             sys.exit()
     if event.type==p.MOUSEBUTTONDOWN:
            x,y=p.mouse.get_pos()
            p.draw.aaline(back,(225,0,0),(600/2,700/2),(x,y))
            back.set_at((x,y),rgb)
     p.display.update()        
             
     
     
