import pygame 
import sys 

pygame.init() 

screen = pygame.display.set_mode((1100,600))
screen.fill((255,255,255))  

colorwhite = (255,255,255) 
colorblack = (0, 0, 0)
colorlight = (170,170,170) 
colordark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Consolas',37)
bigfont = pygame.font.SysFont('Consolas', 45)
  
# rendering a text written in 
# this font 
textsolo = smallfont.render('Solo' , True , colorwhite)
textduo = smallfont.render('Duo' , True , colorwhite)
title = bigfont.render('Power Play' , True , colorblack)

running = True
  
while running: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            running = False 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #si on click sur les boutons 
            if width/3 <= mouse[0] <= width/3+100 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit() 
            elif width/2 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+40:
                pygame.quit()      
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple
    pygame.init() 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade  
    pygame.draw.rect(screen,colordark,[width/3,height/2,100,40])
    pygame.draw.rect(screen,colordark,[width/2,height/2,100,40])
    
    if width/3 <= mouse[0] <= width/3+100 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,colorlight,[width/3,height/2,100,40])
    
    elif width/2 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,colorlight,[width/2,height/2,100,40])
      
    #définir le texte
    screen.blit(textsolo , (width/3+10,height/2)) 
    screen.blit(textduo , (width/2+20,height/2))
    screen.blit(title , (width/3+20,height/10))
      
    # updates the frames of the game 
    pygame.display.update() 
