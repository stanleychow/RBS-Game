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

    # Draw some text
    font = pygame.font.SysFont(None, 40)
    text_img = font.render("R : Reload | B : Block | S : Shoot", True, GREEN)
    screen.blit(text_img, (100, 500))

    # Update the game display
    pygame.display.update()

    keys = pygame.key.get_pressed()
    computer_rbs = ['r', 'b', 's']
    # Update the player
    # If user presses R to Reload
    if keys[pygame.K_r]:
        enemy_move = random.choice(computer_rbs)
        #And computer Reloads
        if enemy_move == "r":
            user_ammo += 1
            computer_ammo += 1
        #And computer Blocks
        if enemy_move == "b":
            user_ammo += 1
        #And computer Shoots
        if enemy_move == "s":
            if computer_ammo > 0:
            user_life -= 1
            computer_ammo -= 1
            if computer_ammo <= 0:
                user_ammo += 1

    #If user presses B to Block
    if keys[pygame.K_b]:
        enemy_move = random.choice(computer_rbs)
        #And computer Reloads
        if enemy_move == "r":
            computer_ammo += 1
        #And computer Blocks
        if enemy_move == "b":
            pass
        #And computer Shoots
        if enemy_move == "s":
            computer_ammo -=1

    #If user presses S to Shoot   
    if keys[pygame.K_s]:
        enemy_move = random.choice(computer_rbs)
        #And computer Reloads
        if enemy_move == "r":
            if user_ammo > 0:
                user_ammo -= 1
                computer_life -= 1
            if user_ammo <= 0:
                computer_ammo += 1
        #And computer Blocks
        if enemy_move == "b":
            if user_ammo > 0:
                user_ammo -=1
            if user_ammo <= 0:
                pass
        #And computer Shoots
        if enemy_move == "s":
            if user_ammo > 0:
                if computer_ammo > 0:
                    user_ammo -= 1
                    computer_ammo -= 1
                if computer_ammo <=0:
                    user_ammo -=1
                    computer_life -= 1
            if user_ammo <= 0:
                if computer_ammo > 0:
                    computer_ammo -= 1
                if computer_ammo <=0:

        
    

# Done! Time to quit.
pygame.quit()