"""
file containing all sort/display functions for menu options
"""
# imports
import pandas as pd

# constants
DATA_PATH = "unite_data.xlsx"  # excel data sheet
PKMN_TYPES = ['Attacker', 'Defender', 'All-rounder', 'Speedster', 'Support']
PKMN_STATS = ['Offense', 'Endurance', 'Mobility', 'Scoring', 'Support']

pkmn_df = pd.read_excel(DATA_PATH, sheet_name="Pokemon")  # read data into pandas dataframe


# Main Menu Display
def main_menu():
    print("\n          Main Menu\n"
          "============options===========\n"
          "- Main menu: 'M'\n"
          "- Pokemon by Type: 'T'\n"
          "- Pokemon by Top Stat: 'S'\n"
          "- Pokemon by Name: 'N'\n"
          # "- Help: 'H' or 'help'\n"
          "- Quit: 'Q' or 'quit'\n")


def pkmn_by_type():
    """
    print sorted table of pokemon based on type
    :return:
    """
    # description
    print("""
    
    What type of pokemon do you want to look for?
    options: 'Attacker', 'Defender', 'Speedster', 'All-Rounder', 'Support'""")
    while True:
        type_selection = input("type >>>").casefold().capitalize()

        if type_selection in PKMN_TYPES:  # check to see if type is valid
            # pandas dataframe
            # - pull all pokemon that match the selected type
            # - select all rows and select columns for data display
            sorted_types = pkmn_df[pkmn_df['Type'] == type_selection]\
                           .loc[:, ['Name', 'Difficulty', 'Range', 'Style', 'Offense',
                                    'Endurance', 'Mobility', 'Scoring', 'Support']]
            sans_index = sorted_types.to_string(index=False)  # remove index for display
            print(f"\n{sans_index}\n")
            # end loop when type is found and printed
            break
        else:  # loop for valid selection
            print("\n*** invalid input, try again ***\n")


# display top 10 pokemon of selected stat
def pkmn_by_stat():
    """
    print sorted table of pokemon based on top stat
    :return:
    """
    # description
    print("""
    
    Which stat would you like to sort by?
    options: 'Offense', 'Endurance', 'Mobility', 'Scoring', 'Support'""")

    while True:
        stat_selection = input("stat >>>").casefold().capitalize()

        if stat_selection in PKMN_STATS:  # check to see if type is valid
            # pandas dataframe
            # - sort by selected value in descending order
            # - pull only the top 10 results
            sorted_stats = pkmn_df[['Name', 'Type', 'Offense', 'Endurance', 'Mobility', 'Scoring', 'Support']] \
                .sort_values(stat_selection, ascending=False)\
                .nlargest(10, stat_selection)
            sans_index = sorted_stats.to_string(index=False)  # remove index for display
            print(f"\n{sans_index}\n")
            break
        else:  # loop for valid selection
            print("\n*** invalid input, try again ***\n")



# def pkmn_by_name(selection):
