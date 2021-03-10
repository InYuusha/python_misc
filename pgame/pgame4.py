import pygame as p
import sys
from pygame.locals import*
class Player:
    x=10
    y=10
    direction=1
    length=200
    speed=1
    def moveright(self):
        self.x=self.x+self.speed
    def moveleft(self):
        self.x=self.x-self.speed
    def moveup(self):
        self.y=self.y-self.speed
    def movedown(self):
        self.y=self.y+self.speed

class app:
    windowwidth=800
    windowheight=600
  
    def __init__(self):
        self.player=Player()
        
    def on_init(self):
        p.init()
        
        self.surface=p.display.set_mode((self.windowwidth,self.windowheight))
        p.display.set_caption("Snake Eater")
        self.running=True
        self.image=p.image.load("C:\\Users\\op\\Desktop\\ball.png")
        
   
        
        
        
    def on_event(self,event):
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
        
    def on_render(self):
        
        self.surface.fill((255,0,0))
       
     
            
        self.surface.blit(self.image,(self.player.x,self.player.y))
        p.display.flip()
        
    def on_cleanup(self):
        p.quit()
        
    def on_execute(self):
            self.on_init()       
     
            while True:
                
                
                self.on_render()
                for event in p.event.get():
                    self.on_event(event)
                
               
                
                keys=p.key.get_pressed()

                if (keys[K_RIGHT]):
                    self.player.moveright()

                if (keys[K_LEFT]):
                    self.player.moveleft()
                    
                if (keys[K_UP]):
                    self.player.moveup()
                    
                if (keys[K_DOWN]):
                    self.player.movedown()
                    
             
               
                    
            self.on_cleanup()


theapp=app()
theapp.on_execute()
                    
                    
         
        
