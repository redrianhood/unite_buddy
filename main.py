#!/usr/bin/env python3
"""
Pokemon Unite data buddy
"""

# import statements
import pandas as pd
# local imports
from bookends import welcome, goodbye
from options import main_menu, pkmn_by_type, pkmn_by_stat, pkmn_by_name


def menu_logic():
    # respond to user input
    while True:
        menu_choice = input(">>> ").lower()  # take input and convert to lowercase

        # return to the main menu
        if menu_choice == 'm' or menu_choice == 'menu':
            main_menu()
        # display pokemon table by the type it is
        elif menu_choice == 't' or menu_choice == 'type':
            pkmn_by_type()
        # display pokemon table by top stats
        elif menu_choice == 's' or menu_choice == 'stat':
            pkmn_by_stat()
        # display an individual pokemon's data
        elif menu_choice == 'n' or menu_choice == 'name':
            pkmn_by_name()
        elif menu_choice == 'h' or menu_choice == 'help':
            print("help menu in development")
        elif menu_choice == 'q' or menu_choice == 'quit':
            goodbye()
            break
        # account for invalid menu selection
        else:
            print("\nInvalid input, please try again\n"
                  "Type 'M' for menu or 'H' for help:\n")


def main():
    """ runtime """
    welcome()  # display welcome banner and message
    main_menu()
    menu_logic()


if __name__ == "__main__":
    main()
