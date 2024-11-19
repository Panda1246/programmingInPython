import game
import argparse
import configparser
import logging

parser = argparse.ArgumentParser(
    description="The program is a turn-based simulation of a wolf and sheep, where the wolf's goal is to eat the sheep")

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
logger = logging.getLogger()
if args.log:
    logging.basicConfig(filename='chase.log', filemode='w', level=args.log)

try:
    file_json = open(r"pos.json", "w")
except:
    logger.critical(f"pos.json does not open")

try:
    file_csv = open(r"alive.csv", "w", newline='')
except:
    logger.critical(f"alive.csv does not open")

if args.config:
    config = configparser.ConfigParser()
    config.read(args.config)
    try:
        config.read(args.config)
        arguments_list["move_dist_wolf"] = float(config["Wolf"].get("MoveDist"))
        arguments_list["move_dist_sheep"] = float(config["Sheep"].get("MoveDist"))
        arguments_list["init_pos_limit"] = float(config["Sheep"].get("InitPosLimit"))
        logger.debug(
            f"Config loaded from {args.config}, Sheep values - MoveDist{arguments_list['move_dist_sheep']}, InitPosLimit{arguments_list['init_pos_limit']}; Wolf values - MoveDist{arguments_list['move_dist_wolf']}")
    except:
        logger.warning(f"Config file was not loaded")
if args.rounds:
    arguments_list["max_number_rounds"] = args.rounds
if args.sheep:
    arguments_list["sheep_alive"] = args.sheep

game = game.Game(**arguments_list)


game.play(file_json, file_csv, args.wait)

file_json.close()
file_csv.close()
