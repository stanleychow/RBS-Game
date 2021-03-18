# import pygame
#GAME LOGIC
#random module
import random 

#starting values for user and computer ammo and life
user_ammo = 1
user_life = 1
computer_ammo = 1
computer_life = 1

#starting game logic
print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
computer_rbs = random.choice(['Reload', 'Block', 'Shoot'])

if user_rbs == "R" and computer_rbs == "Reload":
    user_ammo +=1 
    computer_ammo +=1
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "R" and computer_rbs == "Block":
    user_ammo += 1
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "R" and computer_rbs == "Shoot":
    user_life = 0
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "B" and computer_rbs == "Reload": 
    computer_ammo +=1
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "B" and computer_rbs == "Block":
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "B" and computer_rbs == "Shoot":
    computer_ammo -= 1
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "S" and computer_rbs == "Reload": 
    user_ammo -= 1
    computer_life = 0
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "S" and computer_rbs == "Block":
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")
elif user_rbs == "S" and computer_rbs == "Shoot":
    computer_ammo -= 1
    user_ammo -= 1
    print("User Ammo/Life: " + str(user_ammo) + " / " + str(user_life) + " | Computer Ammo/Life: " + str(computer_ammo) + " / " + str(computer_life))
    user_rbs = input("Reload(R), Block(B), or Shoot(S)? ")

if user_life == 0 or computer_ammo == 3:
    print('You lost!')
elif computer_life == 0 or user_ammo == 3:
    print('You won!')


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