import pygame
from settings import *
from raycasting import raycasting

class Drawing:
    def __init__(self, sc) -> None:
        self.sc = sc

    def background(self):
        pygame.draw.rect(self.sc, SKYBLUE, (0,0,WIDTH, HEIGHT))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    
    def world(self, player_pos, player_angle):
        raycasting(self.sc, player_pos, player_angle)