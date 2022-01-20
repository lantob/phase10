from random import randrange
from source.game import Game

import logging
import argparse
import sys

log = logging.getLogger("ste")



def main(parameters):
    log.debug("Initialize Game")
    game = Game()
    game.cycle()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--debug", action="store_true")
    parser.add_argument("--start", action="store_true")

    parameters = parser.parse_args()

    if parameters.debug:
        log.info("Enable Debug Output")
        logging.basicConfig(level=logging.DEBUG)
    else:
        log.info("Disabled Debug output")


    if parameters.start:
        main(parameters)

