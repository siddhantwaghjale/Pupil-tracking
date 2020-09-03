import pygame
import sys
import random
import time

#checking initializing errors
check_errors = pygame.init()
if check_errors[1] > 0 :
	print("{!} Executred {0} errors! Exiting...!".format(check_errors))
	sys.exit(-1)
else :
	print("{!} Pygame successfully initialized")
	
#play surface
playSurface = pygame.display.set_mode((1500,720))
pygame.display.set_caption('gaze tracker')
#color
dimgrey = pygame.Color(148,148,148)
green = pygame.Color(0,255,0)
black = pygame.Color(0,0,0) 
white = pygame.Color(255,255,255) 
yellow = pygame.Color(255,255,0) 
blue = pygame.Color(0,255,255)
grey = pygame.Color(220,220,220)

#FPS controller
fpsController = pygame.time.Clock()


#position
pos1=[100,50]
pos2=[100,270]
pos3=[100,490]
pos4=[550,50]
pos5=[550,270]
pos6=[550,490]
pos7=[1000,50]
pos8=[1000,270]
pos9=[1000,490]
font = pygame.font.SysFont(None,60)

def findRect(x, y) :
        if pygame.mouse.get_pos()[0] > x and pygame.mouse.get_pos()[0] < (x+350) and pygame.mouse.get_pos()[1] > y and pygame.mouse.get_pos()[1] < (y+150):
                return True
        else:
                return False
def message(msg,color,x,y):
        screen_text=font.render(msg,True,color)
        playSurface.blit(screen_text,[x,y])
        
while True :
        for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                        pygame.quit()
                        sys.exit()
        playSurface.fill(grey)
        #image = pygame.image.load("1.jpg")
        #rect = image.get_rect()
        #playSurface.blit(image,rect)
        #rect.topleft=(300,50)
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos1[0],pos1[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos2[0],pos2[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos3[0],pos3[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos4[0],pos4[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos5[0],pos5[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos6[0],pos6[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos7[0],pos7[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos8[0],pos8[1],350,150))
        pygame.draw.rect(playSurface,dimgrey,pygame.Rect(pos9[0],pos9[1],350,150))
        message("Volume Up",black,160,105)
        message("Volume Down",black,590,105)
        message("Toggle Mute",black,1060,105)
        message("Brightness Up",black,130,325)
        message("Brightness Down",black,550,325)
        message("Alert",black,1100,325)
        message("Play",black,200,545)
        message("Pause",black,640,545)
        message("Skip",black,1090,545)
        
        #if findRect(100,50):
               # image = pygame.image.load("rege.jpg").convert()
                #image = pygame.transform.scale(image, (350, 150))
                #rect = image.get_rect()
                #rect.topleft=(100,50)
                #playSurface.blit(image,rect)
               #pygame.draw.rect(playSurface,white,pygame.Rect(pos1[0],pos1[1],350,150))
        if findRect(100,50):
                 pygame.draw.rect(playSurface,white,pygame.Rect(pos1[0],pos1[1],350,150))
                 message("Volume Up",black,160,100)
        if findRect(100,270):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos2[0],pos2[1],350,150))
                message("Brightness Up",black,130,325)
        if findRect(100,490):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos3[0],pos3[1],350,150))
                message("Play",black,200,545)
        if findRect(550,50):
                 pygame.draw.rect(playSurface,white,pygame.Rect(pos4[0],pos4[1],350,150))
                 message("Volume Down",black,590,100)
        if findRect(550,270):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos5[0],pos5[1],350,150))
                message("Brightness Down",black,550,325)
        if findRect(550,490):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos6[0],pos6[1],350,150))
                message("Pause",black,640,545)
        if findRect(1000,50):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos7[0],pos7[1],350,150))
                message("Toggle Mute",black,1060,100)
        if findRect(1000,270):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos8[0],pos8[1],350,150))
                message("Alert",black,1100,325)
        if findRect(1000,490):
                pygame.draw.rect(playSurface,white,pygame.Rect(pos9[0],pos9[1],350,150))
                message("Skip",black,1090,545)
        pygame.display.flip()
        fpsController.tick(20)
