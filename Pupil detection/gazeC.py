import cv2
import numpy as np
import ClassyVirtualReferencePoint as ClassyVirtualReferencePoint
import ransac
import pygame as pygame
import pygamestuff
import eyeDetect as ey

BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)

 
x = gazeCoords[0,0]
y = gazeCoords[0,1]
print x,"  ", y;


im = cv2.imread('WS.png')
cv2.imshow("window", im)
pygame.draw.circle(im, BLUE,(x,y), radius, width=0)
