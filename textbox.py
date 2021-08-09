# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:23:47 2021

@author: Kevi023
"""
import pygame
import sys

enter = False

class Textbox:
    def __init__(self, w, h, x, y, callback = None):
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        self.text = ""
        self.callback = callback
        self.font = pygame.font.SysFont("Arial", 30)
        self.__surface = pygame.Surface((w, h))
    
    def draw(self, dest_surf):
        text_surf = self.font.render(self.text, True, (255,255,255))
        dest_surf.blit(self.__surface, (self.x, self.y))
        dest_surf.blit(text_surf, (self.x, self.y + (self.height - text_surf.get_height())), (0, 0, self.width, self.height))
        
    def key_down(self, event):
        unicode = event.unicode
        key = event.key
        
        if key == 8:
            if self.text == '':
                pass
            else:
                self.text = self.text[:-1]
            return 
        elif key == 301:
            return
        elif key == 13:
            if self.callback is not None:
                global enter
                self.callback()
                enter = True
            return
        else:
            if unicode != "":
                char = unicode
            else:
                char = chr(key)
            self.text += char            
            return 

def callback():
    print("enter test")
    return True

def main():
    pygame.init()
    winSur = pygame.display.set_mode((640, 480))
    # 创建文本框
    text_box = Textbox(200, 30, 200, 200, callback=callback)
 
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                text_box.key_down(event)
        pygame.time.delay(33)
        winSur.fill((100, 100, 100))
        text_box.draw(winSur)
        pygame.display.flip()
 
 
if __name__ == '__main__':
    main()
 
