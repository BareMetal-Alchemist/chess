import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Clock to control frame rate
clock = pygame.time.Clock()

# Colors (RGB)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main game loop
running = True
while running:
    # Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill(WHITE)

    # Draw a blue circle at the center
    pygame.draw.circle(screen, BLUE, (WIDTH // 2, HEIGHT // 2), 50)

    # Update display
    pygame.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)


