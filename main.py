# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:38:10 2021

@author: Kevi023
"""

import bird
import pipeline
import pygame
import sys 
                 
def displayScore():
    score_text = "current score:" + str(pipeline.score)
    score_font = pygame.font.SysFont('Arial', 20)
    score_surf = score_font.render(score_text, 1, (200, 200, 200))
    screen.blit(score_surf, [0, 0])
    pygame.display.flip()
    
def readyToStart():
    clock.tick(60)
    
    background = pygame.image.load('image/background.png')
    start_icon = pygame.image.load('image/button_play.png')
    ready_bird = pygame.image.load('image/bird_wingDown.png')
    screen.blit(background, (0, 0))
    screen.blit(start_icon, (86, 350))
    screen.blit(ready_bird, (50, 250))
    pygame.display.flip()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (86 <= mouse_x <= 202) and (350 <= mouse_y <= 420):
                return True
            else:
                return False
    pygame.display.flip()
        
def createMap():
    global up_pip_pos
    global down_pip_pos
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    
    screen.blit(Pipeline.down_pipe, (Pipeline.wallx, pipeline.down_pip_pos))
    screen.blit(Pipeline.up_pipe, (Pipeline.wallx, pipeline.up_pip_pos))
    Pipeline.__Movement__()
    
    if Bird.dead:
        Bird.status = 2
    else:
        if Bird.status == 1:
            Bird.status = 0
        elif Bird.status == 0:
            Bird.status = 1
        
    
    screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY - 12)) #调整贴图的位置，使得其碰撞位置显示更加准确
    Bird.__Movement__()
    
    displayScore()

    
def checkDead():
    upPipeRect = pygame.Rect(Pipeline.wallx, pipeline.up_pip_pos,
                             Pipeline.up_pipe.get_width() - 10,
                             Pipeline.up_pipe.get_height())
    
    downPipeRect = pygame.Rect(Pipeline.wallx, pipeline.down_pip_pos, 
                               Pipeline.down_pipe.get_width() - 10,
                               Pipeline.down_pipe.get_height())
    
    if upPipeRect.colliderect(Bird.birdRect) or downPipeRect.colliderect(Bird.birdRect):
        Bird.dead = True
        return True
    elif not -30 < Bird.birdRect[1] < height:
        Bird.dead = True
        return True
    else:
        return False

def getResult():
    final_text1 = "Game Over"
    final_text2 = "Your final score is:  " + str(pipeline.score)
    ft1_font = pygame.font.SysFont("Arial", 30)                                      # 设置第一行文字字体
    ft1_surf = ft1_font.render(final_text1, 1, (242, 3, 36))                             # 设置第一行文字颜色
    ft2_font = pygame.font.SysFont("Arial", 25)                                      # 设置第二行文字字体
    ft2_surf = ft2_font.render(final_text2, 1, (253, 177, 6))                            # 设置第二行文字颜色
    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  # 设置第一行文字显示位置
    screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置第二行文字显示位置
    pygame.display.flip()   

def main(start):  
    while not start:
        start = readyToStart()
                   
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
                Bird.jump = True
                Bird.gravity = 4
                Bird.jumpSpeed = 10
        background = pygame.image.load('image/background.png')
    
        if checkDead():
            getResult()
        else:
            createMap()
     
        pygame.display.flip()
    
    pygame.quit()                  


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 50)  
    clock = pygame.time.Clock()

    size = width, height = 288, 512
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('image/background.png')
    pygame.display.set_caption("Flappy Bird Beta")
    
    Pipeline = pipeline.Pipeline()
    Bird = bird.Bird()
    start = readyToStart()
    
    main(start)