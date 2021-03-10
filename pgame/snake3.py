import pygame as p
import sys
import time as t
import random as r

p.init()

back=p.display.set_mode((728,480))
p.display.set_caption('Snake Eater')
fps=p.time.Clock()


font=p.font.SysFont("times new roman",30)



   

        
        
def message(msg,rect):
    
    text=font.render(msg,True,(0,0,0))
    
    back.blit(text,rect)
def gameLoop():
    x_change,y_change=0,0
    x,y=300,200
    score=0
   
   
    game_over=False
    game_close=False
    x_food=round(r.randrange(50,690))
    y_food=round(r.randrange(50,430))
  
    
    

    while not game_over:
       back.fill((0,125,0,100))
  
    
       while game_close==True:
        
            message("You Lost Press C - continue Q - Quit",[50,200,80,80])
    
            p.display.update()
            for event in p.event.get():
               if event.type==p.KEYDOWN:
                  if event.key==ord('q'):
                     game_over=True
                     game_close=False
                  elif event.key==ord('c'):
                     gameLoop()
                
        
        
        
  
       for event in p.event.get():
           if event.type==p.QUIT:
              p.quit()
              sys.exit()
           elif event.type==p.KEYDOWN:
              if event.key==p.K_UP:
                 y_change=-10
                 x_change=0
                
              elif event.key==p.K_DOWN:
                 y_change=10
                 x_change=0
              elif event.key==p.K_RIGHT:
                 x_change=10
                 y_change=0
              elif event.key==p.K_LEFT:
                 x_change=-10
                 y_change=0
                 
                
     
       
       food_rect=p.draw.rect(back,(255,125,125),[x_food,y_food,20,20])
       snake_rect=p.draw.rect(back,(255,0,0),[x,y,20,20])
      
    
       if (x==0 or x>=728-20) or (y==0 or y>=480-20):
           message("Your Score is :"+str(score),[50,200,80,80])
           p.display.update()
           t.sleep(5)
        
           game_close=True
         
         
         
      
       x+=x_change
       y+=y_change
      
       if snake_rect.colliderect(food_rect):
           x_food=round(r.randrange(50,690))
           y_food=round(r.randrange(50,430))
           score+=1
    
           
          
       
       p.display.update()
       fps.tick(30)

    

   
    t.sleep(3)
    p.quit()
    sys.exit()

gameLoop()    
