import pygame
import random

#Starting values of life and ammo
user_ammo = 1
user_life = 1
computer_ammo = 1
computer_life = 1

#Color constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Welcome to Bullet Bluffer!')

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])