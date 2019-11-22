#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame,math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

BLACK = (0,0,0)
MAGENTA = (255,0,255)
RED = (255,0,0)
GREEN = (0,128,0)
LIME = (0,255,0)
BLUE = (0,0,255)

class Circle(object):
    def __init__(self):
        self.font = pygame.font.Font(None,35)
        
        
    def get_coordinates(self):
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0] - SCREEN_WIDTH / 2
        y = mouse_pos[1] - SCREEN_HEIGHT / 2 - 50
        
        return x,y
        
    def get_degrees(self):
        mouse_pos = self.get_coordinates()
        
        x = mouse_pos[0]
        y = mouse_pos[1]
        
        degrees = 0
        
        if y < 0:
            if x == 0:
                degrees = 90
            elif x > 0:
                tmp = math.atan(abs(y)/abs(float(x)))
                degrees = math.degrees(tmp)
            else:
                tmp = math.atan(abs(y)/abs(float(x)))
                degrees = 180 - math.degrees(tmp)
            
        elif y > 0:
            if x == 0:
                degrees = 270
            elif x > 0:
                tmp = math.atan(abs(y)/abs(float(x)))
                degrees = 360 - math.degrees(tmp)
            else:
                tmp = math.atan(abs(y)/abs(float(x)))
                degrees = 180 + math.degrees(tmp)
                
        elif x < 0:
            degrees = 180
                
        
        return degrees
                
    
    def get_point_pos(self,degrees):
        x = int(SCREEN_WIDTH/2 + math.cos(math.radians(degrees)) * 150)
        y = int(SCREEN_HEIGHT/2 + 50 + math.sin(math.radians(degrees - 180)) * 150)
        
        return x,y
        
        
    def draw(self,screen):
        
        degrees = self.get_degrees()
        
        sine = math.sin(math.radians(degrees))
        cosine = math.cos(math.radians(degrees))
        tangent = math.tan(math.radians(degrees))
        
        text_cos = self.font.render("Cos(" + str(int(degrees)) + ") = " + str(round(cosine,3)) ,True,BLUE)
        text_width = text_cos.get_width()
        screen.blit(text_cos,(SCREEN_WIDTH/2 - text_width/2,0))
        
        text_sin = self.font.render("Sin(" + str(int(degrees)) + ") = " + str(round(sine,3)) ,True,GREEN)
        text_width = text_sin.get_width()
        screen.blit(text_sin,(SCREEN_WIDTH/2 - text_width/2,50))
        
        
        pygame.draw.circle(screen,MAGENTA,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50),150,2)
        pygame.draw.line(screen,MAGENTA,(160,290),(480,290),2)
        pygame.draw.line(screen,MAGENTA,(320,130),(320,450),2)
        
        point_pos = self.get_point_pos(degrees)
        
        pygame.draw.line(screen,BLACK,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50),point_pos,2)
        pygame.draw.line(screen,LIME,point_pos,(point_pos[0],SCREEN_HEIGHT/2+50),2)
        pygame.draw.line(screen,BLUE,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2+50),(point_pos[0],SCREEN_HEIGHT/2+50),2)
        
        pygame.draw.circle(screen,RED,point_pos,5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Unit Circle")
    done = False
    clock = pygame.time.Clock()
    
    circle = Circle()
    
    #-----Main Loop -------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        screen.fill((255,255,255))
        circle.draw(screen)
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
                

if __name__ == '__main__':
    main()
