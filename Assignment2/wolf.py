from animal import Animal
import logging


class Wolf(Animal):
    def __init__(self, move_dist):
        self.position_x = 0.0
        self.position_y = 0.0
        super().__init__(move_dist)

    def find_closest_sheep(self, sheep_list):
        distance_to_sheep = []
        for sheep in sheep_list:
            if sheep.position_x is None:
                distance_to_sheep.append(float('inf'))
            else:
                distance_to_sheep.append(
                    ((self.position_x - sheep.position_x) ** 2) + ((self.position_y - sheep.position_y) ** 2))
        closest_sheep = sheep_list[distance_to_sheep.index(min(distance_to_sheep))]
        distance_to_closest_sheep = min(distance_to_sheep) ** 0.5
        logging.debug(f"The distance to closest sheep {closest_sheep.sheep_id} is {distance_to_closest_sheep}")
        return closest_sheep, distance_to_closest_sheep

    def move(self, sheep_list, sheeps_alive):
        closest_sheep, distance_to_closest_sheep = self.find_closest_sheep(sheep_list)

        if distance_to_closest_sheep <= self.move_dist:
            self.position_x = closest_sheep.position_x
            self.position_y = closest_sheep.position_y
            print(f"Sheep {closest_sheep.sheep_id} has been eaten")
            closest_sheep.position_x = None
            closest_sheep.position_y = None
            sheeps_alive -= 1
            logging.info(f"Wolf has eaten sheep {closest_sheep.sheep_id}")
        else:
            scale = self.move_dist / distance_to_closest_sheep
            self.position_x += scale * (closest_sheep.position_x - self.position_x)
            self.position_y += scale * (closest_sheep.position_y - self.position_y)
            print(f"Wolf is chasing Sheep {closest_sheep.sheep_id}")
            logging.info(f"Wolf is chasing sheep {closest_sheep.sheep_id}")
        logging.debug(f"Wolf moved to x:{self.position_x}, y:{self.position_y}")
        return sheeps_alive
