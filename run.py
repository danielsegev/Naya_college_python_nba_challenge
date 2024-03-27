import pandas as pd
import urllib.request
from PIL import Image
import io
from IPython.display import display
import random
import os
import sys
import time
import requests
import clues
import import_data
import players_stats
import play_trivia
import main_game


import_data()
select_random_player()
clue_1()
clue_2()
clue_3()
clue_4()
clue_5()
clue_6()
clue_7()
clue_8()
players_stats()
general_stats()
play_game()
choose_first()
choose_next()


# Main function
def main():
    choose_first()
if __name__ == "__main__":
    main()