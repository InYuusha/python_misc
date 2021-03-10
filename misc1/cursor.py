import pygame as p,sys
from pygame.locals import*


class func():
    def __init__(self):
        
       p.init()
       self.fps=p.time.Clock()
       self.back=p.display.set_mode((700,400),p.NOFRAME,32)
       self.cursor=p.image.load("C:\\Users\\op\\Desktop\\ball.png").convert()
       self.x=300
       self.y=300
       self.speed=1
       
    def move_right(self):
        self.x+=self.speed
    def move_left(self):
        self.x-=self.speed
    def move_up(self):
        self.y=self.y-self.speed
    def move_down(self):
        self.y+=self.speed
        
        
        
   
class app:
    def __init__(self):
        self.fun=func()
        
    def on_render(self):
        
        self.fun.back.fill((225,225,225))
        self.fun.back.blit(self.fun.cursor,(self.fun.x,self.fun.y))
        p.display.flip()
        
        
    def work(self):
       
        
       while True:
           self.on_render()
          
           for event in p.event.get():
              if event.type==p.QUIT:
                  p.quit()
                  sys.exit()


                  
           keys=p.key.get_pressed()
              
           if (keys[K_UP]):
                     self.fun.move_up()
                     
           if (keys[K_DOWN]):
                    self.fun.move_down()
           if (keys[K_LEFT]):
                    self.fun.move_left()
           if (keys[K_RIGHT]):
                    self.fun.move_right()
            
            
         
         
           #self.fun.fps.tick(3)

run=app()
run.work()

    

    
    
