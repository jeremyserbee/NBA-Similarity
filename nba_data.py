'''
Jeremy Serbée
nba_data.py
Program that gives you a players' playoff performance most similar to that of the users input
'''

from nba_driver import *


def most_similar(normalized_players):
    '''Identify the player with the most similar playoff
    performance to a user inputted player using normalized data'''

    user_input_found = False
    smallest_dist = float('inf')
    most_similar = ''


    # Prompt the user for a player and season and find it in the normalized data
    while user_input_found == False:
        user_input = input('Choose a player').strip().lower()
        year_input = input('Choose a season').strip()
        for i in normalized_players:
            if (i[0].strip(), i[1].lower().strip()) == (year_input, user_input):
                user_input = i
                user_input_found = True
                break
        if user_input_found == False:
            print('Player not found, lets try this again!')

    # Test each players Euclidean distance from the user inputted player and return the most similar player
    for player in normalized_players:
        if players[player].player != players[user_input].player:
            if euclidean((list(normalized_players[user_input].values())),
                         (list(normalized_players[player].values()))) < smallest_dist:
                smallest_dist = euclidean((list(normalized_players[user_input].values())),
                         (list(normalized_players[player].values())))
                most_similar = player

    return most_similar, smallest_dist


def main():
    normalized_players = normalize_data(players)
    print(most_similar(normalized_players))

main()