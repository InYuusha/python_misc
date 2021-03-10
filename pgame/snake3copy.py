import pygame as p
import sys
import time as t
import random as r

p.init()
color={'red':(255,0,0),'blue':(0,0,255),'green':(0,255,0)}

back=p.display.set_mode((728,480))
p.display.set_caption('Snake Eater')
fps=p.time.Clock()


font=p.font.SysFont("ravie",50)
   

def co():
    return r.choice(list(color.values()))
                    
def message(msg,rect):
    
    text=font.render(msg,True,(0,0,125))
    
    back.blit(text,rect)
    
def gameLoop():
    x,y=200,200
    
    
    snake_list=[[200,200],[200-10,200],[200-2*10,200],[200-3*10,200]]
    snake_pos=[x,y]
    score=0
   
   
    game_over=False
    direct="RIGHT"
   
    changeto="None"
    game_close=False
    x_food=round(r.randrange(50,690))
    y_food=round(r.randrange(50,430))
  
    
    

    while not game_over:
       back.fill((50,0,0))
  
    
       while game_close==True:
            back.fill((125,125,125))
        
            message("You Lost ",[100,100,80,80])
            message(" Press C - continue ",[50,150,80,80])
            message("Q - Quit",[100,250,80,80])
    
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
                 changeto="UP"
                 
              if event.key==p.K_DOWN:
                 changeto="DOWN"
              if event.key==p.K_RIGHT:
                 changeto="RIGHT"
                 
              if event.key==p.K_LEFT:
                 changeto="LEFT"
                 
                 
                

           

       if changeto=="RIGHT" and direct!="LEFT":
           direct="RIGHT"
       if changeto=="LEFT" and direct!="RIGHT":
           direct="LEFT"
       if changeto=="UP" and direct!="DOWN":
           direct="UP"
       if changeto=="DOWN" and direct!="UP":
           direct="DOWN"
         
 
       
    
       
       if direct=="UP":
            snake_pos[1]-=10
       if direct=="DOWN":
           
            snake_pos[1]+=10
       if direct=="RIGHT":
            snake_pos[0]+=10
       if direct=="LEFT":
            snake_pos[0]-=10

            
      
       food_rect=p.draw.rect(back,(255,125,125),[x_food,y_food,12,12])
       snake_list.insert(0,list(snake_pos))
                
       for pos in snake_list:
             c=co()
             
             snake_body=p.draw.rect(back,c,[pos[0],pos[1],12,12])
             
     
      
       head=p.Rect(snake_pos[0],snake_pos[1],20,20)
       if head.colliderect(food_rect):
       
           x_food=round(r.randrange(50,690))
           y_food=round(r.randrange(50,430))
           score+=1
       else:
           
           snake_list.pop()
        

    
       if (snake_pos[0]==0 or snake_pos[0]>=728-20) or (snake_pos[1]==0 or snake_pos[1]>=480-20):
           message("Your Score is :"+str(score),[50,200,80,80])
           p.display.update()
           t.sleep(2)
        
           game_close=True
       for block in snake_list[1:]:
           if (snake_pos[0]==block[0] and snake_pos[1]==block[1]):
               
              message("Your Score is :"+str(score),[50,200,80,80])
              p.display.update()
              t.sleep(2)
        
              game_close=True
           
       

    
       p.display.update()
       fps.tick(20)

    

   
    t.sleep(2)
    p.quit()
    sys.exit()

gameLoop()    
