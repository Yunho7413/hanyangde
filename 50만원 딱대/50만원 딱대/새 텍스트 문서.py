import pygame
import random
import math
pygame.init()

start = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode([500,700])

chchx = 0
chchy = 0
chx = 50
chy = 50
bx = 0
by = 0
chbx = 0
chby= 0               #bx by 위치값 chbx chby 변화값
opening = False
start_ = True
character = pygame.image.load('character.png') #chch 바뀌는값 ch는 위치값
bcmax = False  #맵 끝애 다다르는가?

while start:
    screen.blit(pygame.image.load('background.png'),(bx,by))
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.KEYDOWN:
            if start_ == True:  #시작화면에서 시작
                start_ = False
            if by >= 0:
                print()
            if opening == False and bcmax == False:
                if event.key == pygame.K_LEFT:   #코드 48줄까진 움직이는거
                    chbx = 1.5
                    #chchx = -1.5
                if event.key == pygame.K_RIGHT:
                    #chchx = 1.5
                    chbx = -1.5
                if event.key == pygame.K_UP:
                    #chchy = -1.5
                    chby = 1.5
                if event.key == pygame.K_DOWN:
                    #chchy = 1.5
                    chby = -1.5
        if event.type == pygame.KEYUP:
            chchx = 0
            chchy = 0
            chbx = 0
            chby= 0


    chx += chchx
    chy += chchy
    bx += chbx
    by += chby
    if opening == False :
        screen.blit(character, (chx , chy))
        if start_ == True:
            screen.blit(pygame.image.load('500x70.png'),(0,0))
    pygame.display.flip() 
    clock.tick(60)

