from Assignment2.animal import Animal
import random
import logging


class Sheep(Animal):
    def __init__(self, init_pos_limit, move_dist, sheep_id):
        self.sheep_id = sheep_id
        self.position_x = random.randrange(-init_pos_limit, init_pos_limit)
        self.position_y = random.randrange(-init_pos_limit, init_pos_limit)
        self.move_dist = move_dist
        self.init_pos_limit = init_pos_limit
        super().__init__(move_dist)
        logging.debug(f"Sheep id: {self.sheep_id} was created at x: {self.position_x}, y: {self.position_y}")

    def move(self):
        if self.position_x is not None:
            direction = random.randint(0, 3)
            if direction == 0:
                logging.debug(f"Sheep id: {self.sheep_id} choose to move up")
                self.position_y += self.move_dist
            if direction == 1:
                logging.debug(f"Sheep id: {self.sheep_id} choose to move right")
                self.position_x += self.move_dist
            if direction == 2:
                logging.debug(f"Sheep id: {self.sheep_id} choose to move down")
                self.position_y -= self.move_dist
            if direction == 3:
                logging.debug(f"Sheep id: {self.sheep_id} choose to move left")
                self.position_x -= self.move_dist
            logging.debug(f"Sheep id: {self.sheep_id} moved to x:{self.position_x}, y: {self.position_y}")
