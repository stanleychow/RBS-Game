import pygame
import random

#Starting values of life and ammo
user_ammo = 1
user_life = 1
computer_ammo = 1
computer_life = 1

#Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Welcome to Bullet Bluffer!')

# Set up the drawing window
screen = pygame.display.set_mode([600, 600])

#Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill(WHITE)

    # Draw three greens circles for enemy lives
    pygame.draw.circle(screen, RED, (150, 200), 30, 5)
    pygame.draw.circle(screen, RED, (300, 200), 30, 5)
    pygame.draw.circle(screen, RED, (450, 200), 30, 5)

    # Draw three greens circles for player lives
    pygame.draw.circle(screen, GREEN, (150, 400), 30, 5)
    pygame.draw.circle(screen, GREEN, (300, 400), 30, 5)
    pygame.draw.circle(screen, GREEN, (450, 400), 30, 5)


    # # Draw some text
    # font = pygame.font.SysFont(None, 40)
    # text_img = font.render('Hello, World!', True, GREEN)
    # screen.blit(text_img, (200, 100))

    # Update the game display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()