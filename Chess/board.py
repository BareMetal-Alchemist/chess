import pygame
import sys

#Init
pygame.init()
WIDTH, HEIGHT = 640, 640
SQUARE_SIZE = WIDTH // 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Chess")

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)

pieces = {
    "wpawn": pygame.image.load("pieces/wpawn.png"),
    "bpawn": pygame.image.load("pieces/bpawn.png"),
}