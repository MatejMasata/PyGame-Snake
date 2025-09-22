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

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

snake_body = [pygame.Vector2(((n_width/2) + 0), ((n_height/2) + 0)),
              pygame.Vector2(((n_width/2) + 0), ((n_height/2) + 1)),
              pygame.Vector2(((n_width/2) + 0), ((n_height/2) + 2))]

direction_x = 0
direction_y = 0

# function for generationg random position of food
def placeFood(width: int, height: int, snake_body = list[pygame.Vector2]) -> pygame.Vector2:

    food_pos = pygame.Vector2()
    is_food_on_snake = True

    while is_food_on_snake:
        food_pos.x = random.randint(0, width - 1)
        food_pos.y = random.randint(0, height - 1)

        is_food_on_snake = False

        for body_part in snake_body:
            if food_pos.x == body_part.x and food_pos.y == body_part.y:
                is_food_on_snake = True
                break

    return food_pos

food_pos = placeFood(n_width, n_height, snake_body)


def is_fruit_eaten(food_pos, snake_body):
    if food_pos.x == snake_body[0].x and food_pos.y == snake_body[0].y:
        return True
    else:
        return False
    
def grow_snake(snake_body = list[pygame.Vector2]) -> pygame.Vector2:

    tail_direction_x = snake_body[-1].x - snake_body[-2].x
    tail_direction_y = snake_body[-1].y - snake_body[-2].y

    new_x = snake_body[-1].x + tail_direction_x
    new_y = snake_body[-1].y + tail_direction_y

    new_body_part = pygame.Vector2(new_x, new_y)

    snake_body.append(new_body_part)

    return snake_body
    

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction_y != 1:
                direction_y = -1
                direction_x = 0
            elif event.key == pygame.K_s and direction_y != -1:
                direction_y = 1
                direction_x = 0
            elif event.key == pygame.K_a and direction_x != 1:
                direction_x = -1
                direction_y = 0
            elif event.key == pygame.K_d and direction_x != -1:
                direction_x = 1
                direction_y = 0

    if direction_x != 0 or direction_y != 0:

            new_x = snake_body[0].x + direction_x
            new_y = snake_body[0].y + direction_y

            new_head = pygame.Vector2(new_x, new_y)

            snake_body.insert(0, new_head)
            snake_body.pop()
    
    # Screen wrapping 
        # Handles when player goes out of bounds
    for body_part in snake_body:
        if body_part.x >= n_width:
            body_part.x = 0
        
        if body_part.x < 0:
            body_part.x = n_width - 1
        
        if body_part.y >= n_height:
            body_part.y = 0
        
        if body_part.y < 0:
            body_part.y = n_height - 1

    # Eating food
    if is_fruit_eaten(food_pos, snake_body):
        food_pos = placeFood(n_width, n_height, snake_body)
        snake_body = grow_snake(snake_body)

    # fill the screen with a color
    screen.fill("darkolivegreen3")

    # Drawing FOOD
    pygame.draw.rect(screen, "red", (food_pos.x * squareSize, food_pos.y * squareSize, squareSize, squareSize))

    # Drawing SNAKE
    for body_part in snake_body:
        pygame.draw.rect(screen, "darkolivegreen", (body_part.x * squareSize, body_part.y * squareSize, squareSize, squareSize))

    # Drawing GRID
    for vertical in range(0, screenWidth, squareSize):
        pygame.draw.line(screen, "darkolivegreen4", (vertical, 0), (vertical, screenHeight), width=4)

    for horizontal in range(0, screenHeight, squareSize):
        pygame.draw.line(screen, "darkolivegreen4", (0, horizontal), (screenWidth, horizontal), width=4)



    # flip() the display
    pygame.display.flip()

    clock.tick(6)

pygame.quit()