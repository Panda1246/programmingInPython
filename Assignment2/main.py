'''
import sheep
import wolf
import json
import csv
import argparse

sheep_list=[]
round_number=1
sheeps_alive = 15
file_json = open(r"pos.json", "w")
file_csv = open(r"alive.csv", "w", newline='')
writer = csv.writer(file_csv)

for i in range(sheeps_alive):
    sheep_list.append(sheep.Sheep(10.0, 0.5, i))
wolf = wolf.Wolf(10.0, 1.0)

while sheeps_alive != 0 and round_number<=50:
    for sheep in sheep_list:
        sheep.move()

    sheeps_alive = wolf.move(sheep_list, sheeps_alive)
    print(f"Round {round_number}, wolf position ({round(wolf.position_x,3)}, {round(wolf.position_y,3)}), alive sheeps: {sheeps_alive}")
    to_json={
        "round_no":round_number,
        "wolf_pos":[round(wolf.position_x,3),round(wolf.position_y,3)],
        "sheep_pos":([f"Sheep - id:{sheep.sheep_id} position ({'null' if sheep.position_x is None else sheep.position_x}, {'null' if sheep.position_y is None else sheep.position_y})"for sheep in sheep_list])
    }
    file_json.write(json.dumps(to_json, indent=3))
    writer.writerow([round_number,sheeps_alive])
    round_number+=1
file_json.close()
file_csv.close()


'''
import game
import argparse
import configparser

file_json = open(r"pos.json", "w")
file_csv = open(r"alive.csv", "w", newline='')
parser = argparse.ArgumentParser()

parser.add_argument("-c", "--config", help="an auxiliary configuration file")
parser.add_argument("-l", "--log",
                    help="recording events to a log, where `L`EVEL stands for a log level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)",
                    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
parser.add_argument("-r", "--rounds", help="the maximum number of rounds", type=int)
parser.add_argument("-s", "--sheep", help="the number of sheep", type=int)
parser.add_argument("-w", "--wait",
                    help="pause after displaying basic information about the status of the simulation at the end of each round until a key is pressed",
                    action="store_true", default=False)
args = parser.parse_args()
arguments_list = {}
print(args.config)
if args.config:
    config = configparser.ConfigParser()
    config.read(args.config)
    try:
        config.read(args.config)
        arguments_list["move_dist_wolf"] = float(config["Wolf"].get("MoveDist"))
        arguments_list["move_dist_sheep"] = float(config["Sheep"].get("MoveDist"))
        arguments_list["init_pos_limit"] = float(config["Sheep"].get("InitPosLimit"))
    except:
        print("Plik jest niepoprawny")
if args.rounds:
    arguments_list["max_number_rounds"] = args.rounds
if args.sheep:
    arguments_list["sheep_alive"] = args.sheep

game = game.Game(**arguments_list)

game.play(file_json, file_csv, args.wait)

file_json.close()
file_csv.close()
