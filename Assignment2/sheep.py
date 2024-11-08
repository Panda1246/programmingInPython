from animal import Animal
import random


class Sheep(Animal):
    def __init__(self, init_pos_limit, move_dist, sheep_id):
        self.sheep_id = sheep_id
        self.position_x = random.randrange(-init_pos_limit, init_pos_limit)
        self.position_y = random.randrange(-init_pos_limit, init_pos_limit)
        self.move_dist = move_dist
        super().__init__(init_pos_limit, move_dist)

    def move(self):
         if self.position_x is not None:
            direction = random.randint(0, 3)
            if direction == 0:
                self.position_y += self.move_dist
            if direction == 1:
                self.position_x += self.move_dist
            if direction == 2:
                self.position_y -= self.move_dist
            if direction == 3:
                self.position_x -= self.move_dist

    def log(self):
        return f"Sheep {self.sheep_id}, position_x: {self.position_x}, position_y: {self.position_y}"
