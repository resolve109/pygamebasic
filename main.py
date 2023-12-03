import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load a background image for the map
background_path = "assets/background.png"  # Change to your map image path
background = pygame.image.load(background_path)
background_rect = background.get_rect()

# Load an image using a string reference for the character
character_path = "assets/npc1.png"
character = pygame.image.load(character_path)
character_rect = character.get_rect()

# Set up the clock to control the frame rate
clock = pygame.time.Clock()
running = True
dt = 0

# Movement speed for the main character
speed = 5

# Initial position of the main character
character_x, character_y = 100, 100

# Camera position
camera_x, camera_y = 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input for character movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= speed
    if keys[pygame.K_RIGHT]:
        character_x += speed
    if keys[pygame.K_UP]:
        character_y -= speed
    if keys[pygame.K_DOWN]:
        character_y += speed

    # Update the camera position to follow the character
    camera_x = character_x - (screen_width // 2)
    camera_y = character_y - (screen_height // 2)

    # Fill the screen with the background image
    screen.blit(background, (-camera_x, -camera_y))

    # Blit the character image onto the screen at the character's position relative to the camera
    screen.blit(character, (character_x - camera_x, character_y - camera_y))

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()
