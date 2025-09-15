# Example file showing a circle moving on screen
import pygame
import random

# pygame setup
pygame.init()

n_width = 30
n_height = 30
squareSize = 40

screenWidth = n_width*squareSize
screenHeight = n_height*squareSize
screen = pygame.display.set_mode((screenWidth, screenHeight))

clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

direction_x = 0
direction_y = 0


def placeFood(width: int, height: int, squareSize: int, player_pos = pygame.Vector2) -> pygame.Vector2:
    x = player_pos.x
    y = player_pos.y
    food_pos = pygame.Vector2(x, y)

    while food_pos.x == player_pos.x and food_pos.y == player_pos.y:
        food_pos.x = random.randint(0, width - 1) * squareSize
        food_pos.y = random.randint(0, height - 1) * squareSize

    return food_pos

food_pos = placeFood(n_width, n_height, squareSize, player_pos)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Change direction based on key press
            if event.key == pygame.K_w and direction_y == 0:
                direction_y = -squareSize
                direction_x = 0
            elif event.key == pygame.K_s and direction_y == 0:
                direction_y = squareSize
                direction_x = 0
            elif event.key == pygame.K_a and direction_x == 0:
                direction_x = -squareSize
                direction_y = 0
            elif event.key == pygame.K_d and direction_x == 0:
                direction_x = squareSize
                direction_y = 0

    player_pos.x += direction_x
    player_pos.y += direction_y

    # fill the screen with a color
    screen.fill("darkolivegreen3")

    # Food
    pygame.draw.rect(screen, "red", (food_pos.x, food_pos.y, squareSize, squareSize))

    # Player
    pygame.draw.rect(screen, "darkolivegreen", (player_pos.x, player_pos.y, squareSize, squareSize))

    if food_pos.x == player_pos.x and food_pos.y == player_pos.y:
        food_pos = placeFood(n_width, n_height, squareSize, player_pos)
    
    for vertical in range(0, screenWidth, squareSize):
        pygame.draw.line(screen, "darkolivegreen4", (vertical, 0), (vertical, screenHeight), width=4)

    for horizontal in range(0, screenHeight, squareSize):
        pygame.draw.line(screen, "darkolivegreen4", (0, horizontal), (screenWidth, horizontal), width=4)

    # Screen wrapping 
    # Handles when player goes out of bounds
    if player_pos.x >= screenWidth:
        player_pos.x = 0
    
    if player_pos.x < 0:
        player_pos.x = screenWidth - squareSize

    if player_pos.y >= screenHeight:
        player_pos.y = 0

    if player_pos.y < 0:
        player_pos.y = screenHeight - squareSize

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(6)

pygame.quit()