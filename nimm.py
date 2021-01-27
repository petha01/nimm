"""
File: nimm.py
-------------------------
Add your comments here.
"""

INITIAL_ROCKS = 20
def main():
    number_of_rocks = INITIAL_ROCKS
    player_number = 1
    number_of_player_1_moves = 0
    number_of_player_2_moves = 0

    while number_of_rocks != 0:
        print("There are " + str(number_of_rocks) + " stones left")
        remove_rocks = int(input("Player " + str(player_number) + " would you like to remove 1 or 2 stones? "))

        while (remove_rocks != 1 and remove_rocks != 2):
            remove_rocks = int(input("Please enter 1 or 2: "))

        number_of_rocks -= remove_rocks
        if player_number == 1:
            number_of_player_1_moves += 1
            player_number += 1
        else:
            number_of_player_2_moves += 1
            player_number -= 1
        if number_of_rocks == -1:           #if last player removes 2 rocks when there is 1 rock left
            number_of_rocks += 1
        print("")

    """
    Since Player 1 is starting, if the number of player 1 moves and player 2 moves are equal, player 2 must have taken
    the last rock. So player one wins
    """

    if number_of_player_1_moves == number_of_player_2_moves:
        winner = 1
    else:
        winner = 2
    print("Player " + str(winner) + " wins!")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
