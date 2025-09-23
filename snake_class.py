import pygame

class Snake:

    def __init__(self, init_length: int = 3, init_head_position: pygame.Vector2 = pygame.Vector2(0, 0)):

        self.body = []
        for body_part in range(init_length):
            self.body.append(pygame.Vector2(init_head_position.x, init_head_position.y + body_part))

        self.score = 0

    def move(self, direction: pygame.Vector2):
        if direction.x !=0 or direction.y !=0:
            new_head = self.body[0] + direction

            self.body.insert(0, new_head)
            self.body.pop()

    def wrap(self):
        pass

    def grow(self):
        tail_direction = self.body[-1] - self.body[-2]
        new_body =  self.body[-1] + tail_direction

        self.body.append(new_body)

    def check_collision(self) -> bool:
        pass

    def add_score(self, value: int = 1):
        self.score += value

    def subtract_score(self, value: int = 1):
        self.score -= value

    def get_score(self) -> int:
        return self.score
    
    def draw(self, square_size, color="darkolivegreen"):
        pass