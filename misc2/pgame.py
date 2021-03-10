import pygame as p, os ,sys
from pygame.locals import*
import threading as th
import time as t
import winsound as w
t.sleep(5)
p.init()
fps=p.time.Clock()
s=p.display.set_mode((800,600))

ball=p.image.load("C:\\Users\\op\\Desktop\\ball.png")
ball_rect=ball.get_rect()

brick=p.image.load("C:\\Users\\op\\Desktop\\brick.png")
brick_rect=brick.get_rect()
p.display.set_caption("Bouncing Ball")
font=p.font.Font("freesansbold.ttf",32)
text=  font.render("Game Over",1,(225,125,125))
text_rect=text.get_rect()
text_rect.topleft=(200,300)
back=p.image.load("C:\\Users\\op\\Desktop\\back5.png")
back_rect=back.get_rect()
p.display.set_icon(ball)
sx,sy=(3,3)
bx,by=(24,200)


while True:

    
    s.blit(back,back_rect)
  
    for event in p.event.get():
        if event.type==QUIT:
            p.quit()
            sys.exit()
        elif event.type==MOUSEMOTION:
            mousex,mousey=event.pos
            if mousex<800-131:
                brick_rect.topleft=(mousex,600-25)
            else:
                brick_rect.topleft=(800-131,600-25)
    def lost():
        text.blit(text,text_rect)
      
     
     
        t.sleep(5)
        p.quit()
        sys.exit()

        
    s.blit(brick,brick_rect)
    ball_rect.topleft=(bx,by)
    
    
    bx+=sx
    by+=sy
    if by<=0:
        by=0
        sy=sy*(-1)
    elif by>=600-50:
        lost()
        
        
        

    elif bx<=0:
        bx=0
        sx=sx*(-1)
    elif bx>800-50:
        bx=800-50
        sx=sx*(-1)
        
        
    
    
    s.blit(ball,ball_rect)
    if ball_rect.colliderect(brick_rect):
        by=600-80
        sy*=-1
        
    p.display.update()
    fps.tick(100)
