"""
file containing all sort/display functions for menu options
"""
# imports
import pandas as pd

# constants
DATA_PATH = "unite_data.xlsx"  # excel data sheet
PKMN_TYPES = ['attacker', 'defender', 'all-rounder', 'speedster', 'supporter']

pkmn_df = pd.read_excel(DATA_PATH, sheet_name="Pokemon")  # read data into pandas dataframe


# Main Menu Display
def main_menu():
    print("\n          Main Menu\n"
          "============options===========\n"
          "- Main menu: 'M'\n"
          "- Pokemon by Type: 'T'\n"
          "- Pokemon by Top Stat: 'S'\n"
          "- Pokemon by Name: 'N'\n"
          "- Help: 'H' or 'help'\n"
          "- Quit: 'Q' or 'quit'\n")


# display all pokemon of selected 'type'
def pkmn_by_type(selection):
    if selection not in PKMN_TYPES:
        print("oopsies")
    sorted_types = pkmn_df[pkmn_df['Type'] == selection]\
                   .loc[:, ['Name', 'Difficulty', 'Range', 'Style', 'Offense',
                            'Endurance', 'Mobility', 'Scoring', 'Support']]\
                   .to_string(index=False)
    print(sorted_types)


# display top 10 pokemon of selected stat
def pkmn_by_stat(selection):
    sorted_stats = pkmn_df[['Name', 'Type', 'Offense', 'Endurance', 'Mobility', 'Scoring', 'Support']]\
        .sort_values(selection, ascending=False)\
        .nlargest(10, selection)
    sans_index = sorted_stats.to_string(index=False)
    print(sans_index)


# def pkmn_by_name(selection):
