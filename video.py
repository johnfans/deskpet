import cv2
import time
import pygame
import sys

def init_video(file):
    cap = capture =cv2.VideoCapture(str(file))
    fps=cap.get(cv2.CAP_PROP_FPS)
    counts=cap.get(cv2.CAP_PROP_FRAME_COUNT)
    return (cap,fps,counts)

def video(cap,fps,counts):
    cap.set(cv2.CAP_PROP_POS_MSEC,0)
    c=0
    t=time.time()
    while(cap.isOpened()) and c<counts:
        c=c+1
        ret, frame = cap.read()
        cv2.imshow('pet',frame)
        while not time.time()>=t+c*(1/fps):
            cv2.waitKey(1)
            if cv2.getWindowProperty('pet',0)==-1:
                sys.exit()
            
    return

def sound(file):
    pygame.mixer.init()
    pygame.mixer.music.load(str(file))
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()
    return

if __name__=='__main__':
    cv2.namedWindow('frame')
    sound('keqing_morning.mp3')
    (cap,fps,counts)=init_video('dc1.mp4')
    for i in range(4):
        video(cap,fps,counts)