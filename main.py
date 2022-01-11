#!/usr/bin/env python3
"""
Pokemon Unite data buddy
"""

# import statements
import pandas as pd
# local imports
from welcome import welcome

# constants
DATA_PATH = "unite_data.xlsx"


def main_menu():
    print("\n          Main Menu\n"
          "============options===========\n"
          "-Main menu: 'M'\n"
          "-Pokemon by Type: 'T'\n"
          "-Pokemon by Top Stat: 'S'\n")

    menu_choice = input(">>> ")

    # response logic to user input
    if menu_choice.lower() == 'm':
        main_menu()
    elif menu_choice.lower() == 't':
        # implement pokemon by type search
        # pkmn_by_type()
        main_menu()
    elif menu_choice.lower() == 's':
        # implement pokemon by top stat
        # pkmn_by_stat()
        main_menu()
    else:
        print("invalid input")


def main():
    # be able to read data from .xlsx document and print to console screen
    pokemon_frame = pd.read_excel(DATA_PATH, sheet_name="Pokemon")

    # ###### BELOW is for reference
    # print(pokemon_frame)
    # print(pokemon_frame.shape)
    # sorted_pokemon = pokemon_frame.sort_values(["Offense"], ascending=False)
    # print(sorted_pokemon)

    # display welcome banner and message
    welcome()
    main_menu()

    # menu
    # 'help' : list available commands


if __name__ == "__main__":
    main()
