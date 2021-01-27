"""
File: nimm.py
-------------------------
Add your comments here.
"""

INITIAL_ROCKS = 20
def main():
    print("I will win for sure.")
    number_of_rocks = INITIAL_ROCKS
    player_number = 1
    number_of_player_1_moves = 0
    number_of_player_2_moves = 0
    while number_of_rocks != 0:
        print("There are " + str(number_of_rocks) + " left")
        if player_number == 2:
            remove_rocks = int(input("Player " + str(player_number) + " would you like to remove 1 or 2 stones? "))

            while (remove_rocks != 1 and remove_rocks != 2):
                remove_rocks = int(input("Please enter 1 or 2: "))

        if player_number == 1:
            if (number_of_rocks == 20 or number_of_rocks == 17 or number_of_rocks == 14 or number_of_rocks == 11
                    or number_of_rocks == 8 or number_of_rocks == 5 or number_of_rocks == 2):
                remove_rocks = 1
            if (number_of_rocks == 18 or number_of_rocks == 15 or number_of_rocks == 12 or number_of_rocks == 9
                    or number_of_rocks == 6 or number_of_rocks == 3):
                remove_rocks = 2
            print("I remove " + str(remove_rocks) + " stone")

        number_of_rocks -= remove_rocks
        if player_number == 1:
            number_of_player_1_moves += 1
            player_number += 1
        else:
            number_of_player_2_moves += 1
            player_number -= 1
        if number_of_rocks == -1:           #if last player removes 2 rocks when there is 1 rock left
             number_of_rocks += 1

    """
    Since Player 1 is starting, if the number of player 1 moves and player 2 moves are equal, player 2 must have taken
    the last rock. So player one wins
    """

    if number_of_player_1_moves == number_of_player_2_moves:
        print("I WON (again)")
    else:       #not required XD
        print("Player 2 wins!")





# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
