import pygame, random, math
from vector import *
pygame.init()

WIDTH, HEIGHT = 1000, 800


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('MarchingSquares')