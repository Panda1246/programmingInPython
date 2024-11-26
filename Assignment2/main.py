from game import Game
import argparse
import configparser
import logging


def main():
    parser = argparse.ArgumentParser(
        description="The program is a turn-based simulation of a wolf and sheep, where the wolf's goal is to eat the sheep")

    parser.add_argument("-c", "--config", help="an auxiliary configuration file", default="default.ini")
    parser.add_argument("-l", "--log",
                        help="recording events to a log, where LEVEL stands for a log level (DEBUG, INFO, WARNING, "
                             "ERROR, or CRITICAL)",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])
    parser.add_argument("-r", "--rounds", help="the maximum number of rounds", type=int, default=50)
    parser.add_argument("-s", "--sheep", help="the number of sheep", type=int, default=15)
    parser.add_argument("-w", "--wait",
                        help="pause after displaying basic information about the status of the simulation at the end of "
                             "each round until a key is pressed",
                        action="store_true", default=False)
    args = parser.parse_args()
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

    config = configparser.ConfigParser()
    try:
        config.read(args.config)
        logger.debug(
            f'Config loaded from {args.config}, Sheep values - MoveDist{config["Sheep"].get("MoveDist")}, InitPosLimit{config["Sheep"].get("InitPosLimit")}; Wolf values - MoveDist{config["Wolf"].get("MoveDist")}')
    except:
        logger.critical(f"Config didn't load")
    game = Game(sheep_alive=args.sheep, max_number_rounds=args.rounds,
                move_dist_sheep=float(config["Sheep"].get("MoveDist")),
                move_dist_wolf=float(config["Wolf"].get("MoveDist")),
                init_pos_limit=float(config["Sheep"].get("InitPosLimit")))

    game.play(file_json, file_csv, args.wait)

    file_json.close()
    file_csv.close()


if __name__ == "__main__":
    main()
