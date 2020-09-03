import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 1700, 700
white = 255, 255, 255
screen = pygame.display.set_mode(size)
dimgrey = pygame.Color(148,148,148)
green = pygame.Color(0,255,0)
black = pygame.Color(0,0,0) 
white = pygame.Color(255,255,255) 
yellow = pygame.Color(255,255,0) 
blue = pygame.Color(0,255,255)
grey = pygame.Color(220,220,220)

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
        screen.blit(screen_text,[x,y])

class Crosshair(object):
    def __init__(self, speed = [1, 1], quadratic = True):
        self.quadratic = quadratic
        self.speed = speed
        self.cross = pygame.image.load('gaussianBlur.png')#pygame.image.load('bmpcrosshair.bmp')
        self.crossrect = self.cross.get_rect()
##        print self.crossrect.center, "is the center"
##        print self.crossrect, "is the rect"
##        print self.crossrect.top, "is the top"
##        print self.crossrect.left, "is the left"
        self.result = []
        self.delay = 20
        self.userWantsToQuit = False
        self.draw()

    def draw(self):
        self.remove()
        #could maybe edit the crossrect directly for smoother motions
        #The Rect object has several virtual attributes which can be used to move and align the Rect:
        #top, left, bottom, right
        #topleft, bottomleft, topright, bottomright
        #midtop, midleft, midbottom, midright
        #center, centerx, centery
        #size, width, height
        #w,h
        screen.fill(grey)
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos1[0],pos1[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos2[0],pos2[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos3[0],pos3[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos4[0],pos4[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos5[0],pos5[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos6[0],pos6[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos7[0],pos7[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos8[0],pos8[1],350,150))
        pygame.draw.rect(screen,dimgrey,pygame.Rect(pos9[0],pos9[1],350,150))
        message("Volume Up",black,160,105)
        message("Volume Down",black,590,105)
        message("Toggle Mute",black,1060,105)
        message("Brightness Up",black,130,325)
        message("Brightness Down",black,550,325)
        message("Alert",black,1100,325)
        message("Play",black,200,545)
        message("Pause",black,640,545)
        message("Skip",black,1090,545)
        if findRect(100,50):
                 pygame.draw.rect(screen,white,pygame.Rect(pos1[0],pos1[1],350,150))
                 message("Volume Up",black,160,100)
        if findRect(100,270):
                pygame.draw.rect(screen,white,pygame.Rect(pos2[0],pos2[1],350,150))
                message("Brightness Up",black,130,325)
        if findRect(100,490):
                pygame.draw.rect(screen,white,pygame.Rect(pos3[0],pos3[1],350,150))
                message("Play",black,200,545)
        if findRect(550,50):
                 pygame.draw.rect(screen,white,pygame.Rect(pos4[0],pos4[1],350,150))
                 message("Volume Down",black,590,100)
        if findRect(550,270):
                pygame.draw.rect(screen,white,pygame.Rect(pos5[0],pos5[1],350,150))
                message("Brightness Down",black,550,325)
        if findRect(550,490):
                pygame.draw.rect(screen,white,pygame.Rect(pos6[0],pos6[1],350,150))
                message("Pause",black,640,545)
        if findRect(1000,50):
                pygame.draw.rect(screen,white,pygame.Rect(pos7[0],pos7[1],350,150))
                message("Toggle Mute",black,1060,100)
        if findRect(1000,270):
                pygame.draw.rect(screen,white,pygame.Rect(pos8[0],pos8[1],350,150))
                message("Alert",black,1100,325)
        if findRect(1000,490):
                pygame.draw.rect(screen,white,pygame.Rect(pos9[0],pos9[1],350,150))
                message("Skip",black,1090,545)

        screen.blit(self.cross, self.crossrect)
        pygame.display.flip()

    def drawCrossAt(self, coords):
        self.crossrect.center = coords
        self.draw()

    def move(self):
        self.crossrect = self.crossrect.move(self.speed)
        if self.crossrect.left < 0 or self.crossrect.right > width:
            self.speed[0] = -self.speed[0]
        if self.crossrect.top < 0 or self.crossrect.bottom > height:
            self.speed[1] = -self.speed[1]

    def record(self, x, y):
        cx, cy = self.crossrect.centerx, self.crossrect.centery
        lis = [x, y, cx, cy]
        if self.quadratic == True:
            lis.append([cx * cx, cx * cy, cy * cy])
        self.result.append(lis)

    def record(self, inputTuple):
        self.result.append(list(inputTuple)+[self.crossrect.centerx,self.crossrect.centery])

    def write(self):
        fo = open("1700wxoffsetyoffsetxy.csv", "w")
        for line in self.result:
            print line
            result = ""
            for number in line:
                result += str(number) + str(',')
            fo.write(result + "\n")
        fo.close()

    #collects data, returns true if done looping
    def loop(self):
        self.move()
        pygame.time.delay(self.delay)
        self.draw()

    def remove(self):
        screen.fill(white)
        pygame.display.flip()

    def clearEvents(self):
        pygame.event.clear()

    # Blocks the thread while waiting for a click.
    def getClick(self):
        needClick = True
        while needClick:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.crossrect.center = pos
                    self.draw()
                    needClick = False
                else:
                    continue

    # Returns True, saves position, and draws the crosshairs if a click has occurred.
    # Returns False if not.
    def pollForClick(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.crossrect.center = pos
                self.draw()
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.userWantsToQuit = True
        return False

    def close(self):
        pygame.display.quit()


##ch = Crosshair()
##for i in range(10):
##    pygame.time.delay(100)
##    ch.getClick()


#while 1:
#    pressed = pygame.mouse.get_pressed()
#    if any(pressed):
#        break
#    for event in pygame.event.get():
#        if event.type in (QUIT, pygame.KEYDOWN):
#            break

#    crosshair.draw()
#    pygame.time.delay(10)#miliseconds
#    xoffset = 0
#    yoffset = 0
#    crosshair.record(xoffset, yoffset)
#    crosshair.move()



