import cv2
import time
import pygame
import sys
import random
from video import *


#这里修改鼠标交互条件
def mouseing(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN and x>=300 and x<=700 and y<=650:
        r=random.randint(0,2)
        (cap,fps,counts)=init_video('jessica_touch2.mp4') 
        if r==0:
            sound('touch1.wav')
        if r==1:
            sound('touch2.wav')
        if r==2:
            sound('touch3.wav')
        video(cap,fps,counts)
    if event == cv2.EVENT_LBUTTONDOWN and 300<=x<=600 and y>650 and y<=850:
        (cap,fps,counts)=init_video('jessica_touch1.mp4') 
        sound('touch4.wav')
        video(cap,fps,counts)
    if event == cv2.EVENT_LBUTTONDOWN and x<300:
        r=random.randint(0,1)
        (cap,fps,counts)=init_video('jessica_shootleft.mp4') 
        if r == 0:
            sound('shoot1.wav')
        if r == 1:
            sound('shoot2.wav')
        video(cap,fps,counts)
    if event == cv2.EVENT_LBUTTONDOWN and x>=650:
        r=random.randint(0,1)
        (cap,fps,counts)=init_video('jessica_shootright.mp4') 
        if r == 0:
            sound('shoot1.wav')
        if r == 1:
            sound('shoot2.wav')
        video(cap,fps,counts)

    



