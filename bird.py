# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:41:01 2021

@author: Kevi023
"""

import pygame

class Bird(object):
    def __init__(self):
        self.birdRect = pygame.Rect((50, 250), (40, 20))
        self.birdStatus = [pygame.image.load('image/bird_wingUP.png'),
                           pygame.image.load('image/bird_wingDown.png'),
                           pygame.image.load('image/dead.png')]
        self.status = 0
        self.jump = False
        self.jumpSpeed = 10
        self.gravity = 4
        self.dead = False
        self.birdX = 50
        self.birdY = 250
        
    def __reset__(self):
        self.jumpSpeed = 10
        
    def __Movement__(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
        else:
            self.gravity += 0.1
            self.birdY += self.gravity
        self.birdRect[1] = self.birdY
