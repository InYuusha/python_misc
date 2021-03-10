import pygame as p
from pygame.locals import*
import sys

class Player:
    x=100
    y=100
    
    direction="RIGHT"
    head_pos=[x,y]
    body_pos=[[x,y],[x-50,y],[x-50*2,y],[x-50*3,y]]
    green=p.Color(0,255,0)
    red=p.Color(255,0,0)
    blue=p.Color(0,0,255)
    black=p.Color(0,0,0)
    white=p.Color(255,255,255)
    changeto="RIGHT"
    
    def direct(self):
        
        if self.changeto=="UP" and self.direction!="DOWN":
            self.direction="UP"
        if self.changeto=="DOWN" and self.direction!="UP":
            self.direction="UP"
        if self.changeto=="RIGHT" and self.direction!="LEFT":
            self.direction="RIGHT"
        if self.changeto=="LEFT" and self.direction!="RIGHT":
            self.direction="LEFT"
      

    def movement(self):
        if self.direction=="UP":
            self.head_pos[1]=self.head_pos[1]-10
        if self.direction=="DOWN":
            head_pos[1]=self.head_pos[1]+10
        if self.direction=="RIGHT":
            self.head_pos[0]=self.head_pos[0]+10
        if self.direction=="LEFT":
            self.head_pos=self.head_pos[0]-10
        
        

class App:
    player=Player()
    window_width=720
    window_height=480
    
  
    
    

    def on_init(self):
       
        p.init()
        self.fps=p.time.Clock()
        self.back=p.display.set_mode((self.window_width,self.window_height))
        p.display.set_caption("Snake Eater")
        

 
      
        
    def display(self):
        self.back.fill(self.player.red)
        self.ball=p.image.load("C:\\Users\\op\\Desktop\\ball.png")
        
        for pos in self.player.body_pos:
            self.back.blit(self.ball,(pos[0],pos[1]))
        p.display.update()   

    def cross_event(self,event):
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
    def on_execute(self):
        self.on_init()
        
        while True:
            
            
           
            
            for event in p.event.get():
                 self.cross_event(event)
                 
            keys=p.key.get_pressed()
            
            if (keys[K_UP]):
                self.player.changeto="UP"
            if(keys[K_DOWN]):
                self.player.changeto="DOWN"
            if(keys[K_RIGHT]):
                self.player.changeto="RIGHT"
            if(keys[K_LEFT]):
                self.player.changeto="LEFT"
                
            self.player.direct()
            self.player.movement()
            self.display() 
            self.fps.tick(30)

theapp=App()
theapp.on_execute()
                
                
        
            
        
                          
        
