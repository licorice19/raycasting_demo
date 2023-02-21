import pygame
from settings import *
from player import Player
import math
from map import *
from raycasting import raycasting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()    
    sc.fill(BLACK)
    
    drawing.background()
    drawing.world(player.pos, player.angle)

    pygame.display.flip()
    clock.tick(FPS)