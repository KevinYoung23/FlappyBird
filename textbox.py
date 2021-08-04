# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:23:47 2021

@author: Kevi023
"""

class textbox:
    def __init__(self, w, h, x, y, callback = None):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""
        self.callback = callback
        self.font = pygame.font.Font('Arial', 30)
        self.__surface = pygame.Surface((w, h))
    
    