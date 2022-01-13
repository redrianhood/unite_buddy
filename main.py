#!/usr/bin/env python3
"""
Pokemon Unite data buddy
"""

# import statements
import pandas as pd
# local imports
from bookends import welcome, goodbye
from options import main_menu, pkmn_by_type, pkmn_by_stat


def menu_logic():
    # respond to user input
    while True:
        menu_choice = input(">>> ").lower()  # take input and convert to lowercase

        # return to the main menu
        if menu_choice == 'm':
            main_menu()
        # display pokemon table by the type it is
        elif menu_choice == 't':
            what_type = input("\nWhat type of pokemon do you want to look for? \n"
                              "options: 'Attacker', 'Defender', 'Speedster', 'All-Rounder', 'Support'\n"
                              ">>>").casefold().capitalize()
            pkmn_by_type(what_type)
        # display pokemon table by top stats
        elif menu_choice == 's':
            what_stat = input("Which stat would you like to sort by?\n>>>").casefold().capitalize()
            pkmn_by_stat(what_stat)
        elif menu_choice == 'h':
            print("help menu in development")
        # quit the program
        elif menu_choice == 'q' or menu_choice == 'quit':
            goodbye()
            break
        # account for invalid menu selection
        else:
            print("Invalid input, please try again\n"
                  "Type 'M' for menu or 'H' for help:\n")


def main():
    """ runtime """
    welcome()  # display welcome banner and message
    main_menu()
    menu_logic()


if __name__ == "__main__":
    main()
