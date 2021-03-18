# import pygame
#GAME LOGIC
user_ammo = 1
user_life = 1
computer_ammo = 1
computer_life = 1

print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
rbs = input("Reload(R), Block(B), or Shoot(S)?")

# if rbs == "R":
#     user_ammo +=1
#     elif rbs == "B":
#         user_



# # Color constants
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)

# # Initialize Pygame
# pygame.init()
# pygame.display.set_caption('Hello Pygame!')

# # Set up the drawing window
# screen = pygame.display.set_mode([500, 500])


# Run until the user asks to quit
# running = True
# while running:
#     # Advance the clock
#     pygame.time.delay(20)

#     # Did the user click the window close button?
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill screen with white
#     screen.fill(WHITE)

#     # Draw a blue square
#     pygame.draw.rect(screen, BLUE, (200, 200, 50, 50))

#     # Draw a red circle
#     pygame.draw.circle(screen, RED, (300, 300), 50, 5)


#     # Draw some text
#     font = pygame.font.SysFont(None, 40)
#     text_img = font.render('Hello, World!', True, GREEN)
#     screen.blit(text_img, (200, 100))

#     # Update the game display
#     pygame.display.update()

# # Done! Time to quit.
# pygame.quit()