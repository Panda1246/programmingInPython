import csv
import json
from wolf import Wolf
from sheep import Sheep
import logging


class Game:
    def __init__(self, sheep_alive=15, max_number_rounds=50, move_dist_sheep=0.5,
                 move_dist_wolf=1.0, init_pos_limit=10.0):
        self.sheep_alive = sheep_alive
        self.max_number_rounds = max_number_rounds
        self.move_dist_sheep = move_dist_sheep
        self.move_dist_wolf = move_dist_wolf
        self.init_pos_limit = init_pos_limit

    def play(self, file_json, file_csv, wait):
        sheep_list = []
        round_number = 1
        writer = csv.writer(file_csv)
        for i in range(self.sheep_alive):
            sheep_list.append(Sheep(self.init_pos_limit, self.move_dist_sheep, i))
        logging.info("All sheeps are created")
        wolf = Wolf(self.move_dist_wolf)

        while self.sheep_alive != 0 and round_number <= self.max_number_rounds:
            logging.info(f"Round {round_number} has started")
            for sheep in sheep_list:
                sheep.move()
            logging.info("All sheeps have moved")

            self.sheep_alive = wolf.move(sheep_list, self.sheep_alive)
            logging.info("Wolf has moved")
            print(
                f"Round {round_number}, wolf position ({round(wolf.position_x, 3)}, {round(wolf.position_y, 3)}), sheep"
                f"s alive: {self.sheep_alive}")
            to_json = {
                "round_no": round_number,
                "wolf_pos": [round(wolf.position_x, 3), round(wolf.position_y, 3)],
                "sheep_pos": ([
                    f"Sheep - id:{sheep.sheep_id} position ({'null' if sheep.position_x is None else sheep.position_x},"
                    f"{'null' if sheep.position_y is None else sheep.position_y})"
                    for sheep in sheep_list])
            }
            file_json.write(json.dumps(to_json, indent=3))
            logging.debug(f"Information was saved to pos.json")
            writer.writerow([round_number, self.sheep_alive])
            logging.debug(f"Information was saved to alive.csv")
            round_number += 1
            logging.info(f"Round is going to end, Sheeps alive: {self.sheep_alive}")
            if wait is True:
                input()
        logging.info("Simulation is over")
