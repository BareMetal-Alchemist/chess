import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pygame Window")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, (WIDTH // 2, HEIGHT // 2), 50)


    pygame.display.flip()

    clock.tick(60)

    pygame.quit()
    sys.exit()