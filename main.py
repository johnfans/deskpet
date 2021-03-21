import cv2
import time
import pygame
import sys
import json
import random
from conf import *
from video import *
from mouse import *



cv2.namedWindow('pet')
(cap,fps,counts)=init_video('jessica_start.mp4')
if 4<=time.localtime()[3]<=11:
    sound('jessica_morn.wav')
else:
    sound('jessica_start.wav')
video(cap,fps,counts)
cv2.setMouseCallback('pet',mouseing)
(cap,fps,counts)=init_video('jessica_default.mp4')
while True:
    video(cap,fps,counts)