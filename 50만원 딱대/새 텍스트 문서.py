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
opening = True
character = [pygame.image.load('character.png'),chx,chy,chchx,chchy]

while start:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.KEYDOWN:
            if opening == False:
                if event.key == pygame.K_LEFT:
                    chchx = -1.5
                if event.key == pygame.K_RIGHT:
                    chchx = 1.5
            if event.key == pygame.K_0:
                    opening = True
            if event.key == pygame.K_1:
                    opening = False
        if event.type == pygame.KEYUP:
            chchx = 0

    character[1] += chchx
    if opening == False:
        screen.blit(pygame.image.load('500x70.png'),(0,0))
        screen.blit(character[0], (character[1] , character[2]))
    pygame.display.flip() 
    clock.tick(60)

