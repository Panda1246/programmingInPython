import csv
import json
from wolf import Wolf
from sheep import Sheep


class Game(object):
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
        wolf = Wolf(self.move_dist_wolf)

        while self.sheep_alive != 0 and round_number <= self.max_number_rounds:
            for sheep in sheep_list:
                sheep.move()

            self.sheep_alive = wolf.move(sheep_list, self.sheep_alive)
            print(
                f"Round {round_number}, wolf position ({round(wolf.position_x, 3)}, {round(wolf.position_y, 3)}), alive sheeps: {self.sheep_alive}")
            to_json = {
                "round_no": round_number,
                "wolf_pos": [round(wolf.position_x, 3), round(wolf.position_y, 3)],
                "sheep_pos": ([
                    f"Sheep - id:{sheep.sheep_id} position ({'null' if sheep.position_x is None else sheep.position_x}, {'null' if sheep.position_y is None else sheep.position_y})"
                    for sheep in sheep_list])
            }
            file_json.write(json.dumps(to_json, indent=3))
            writer.writerow([round_number, self.sheep_alive])
            round_number += 1
            if wait is True:
                input()
