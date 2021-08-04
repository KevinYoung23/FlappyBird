# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:43:14 2021

@author: Kevi023
"""
import pygame
import random
import time

score = 0
up_pip_pos = -100   
down_pip_pos = 412
start_time = time.time()

class Pipeline(object):
    def __init__(self):
        self.wallx = 288
        self.down_pipe = pygame.image.load('image/bottomPip.png')
        self.up_pipe = pygame.image.load('image/upPip.png')
        
    def __Movement__(self):
        global start_time
        current_time = time.time()
        if current_time - start_time < 10:
            self.wallx -= 2
        elif current_time - start_time < 20:
            self.wallx -= 4
        else:
            self.wallx -= 6
        if self.wallx < -30:
            global score
            global down_pip_pos
            global up_pip_pos
            up_pip_pos = random.randint(-150, 0)
            down_pip_pos = random.randint(300, 450)
            score += 1
            self.wallx = 288