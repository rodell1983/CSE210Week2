# CSE210 Week 2 Tic Tac Toe
# Robert Odell


# Main function called when the program executes


def main():

    # Holds the default grid values
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Sets current player
    player = "O"

    # Display Game Title
    print("\n------ Tic Tac Toe -------")

    # Main program loop
    while True:

        # Alternate user for X to O and visa versa
        # after each move

        if player == "O":
            player = "X"
        else:
            player = "O"

        # Call print grid
        print_grid(grid)

        loop = True
        while loop:
            # Prompt current player to take their turn
            square = player_turn(player)

            # test if the selection is valid
            # if the move is valid place score
            # if the move is not valid loop
            square_val = get_square_val(square, grid)
            if square_val == "O" or square_val == "X":
                print(f"Try another square")
            else:
                place_score(player, square, grid)
                loop = False

        # Test if there is a winner
        winner = test_win(grid)
        if winner != "":
            if winner == "T":
                print(f"Tie Game")
            else:
                print(f"The winner is {winner}")

            print_grid(grid)

            # Prompt user to play again
            if yes_no_input("Would you like to play again?"):
                main()
            else:
                print("Goodbye")
                return

# Prints the current game grid


def print_grid(grid):
    print()
    for i in range(0, 3):
        print(f"{grid[i][0]} | {grid[i][1]} | {grid[i][2]}")
        if i < 2:
            print("- + - + -")
    print()


# Display prompt for play to select a square

def player_turn(player):

    while True:
        value = input(f"{player}'s turn to choose a square (1-9): ")
        if value.isdigit():
            return value
        else:
            print(f"{value} is not a valid number.")

# Return row and collumn from square number


def get_square(square):

    # set square to integer
    square = int(square)

    # Set row
    if square <= 3:
        row = 0
    elif square > 3 and square <= 6:
        row = 1
    elif square > 6:
        row = 2

    # Set collumn
    if square == 1 or square == 4 or square == 7:
        col = 0
    elif square == 2 or square == 5 or square == 8:
        col = 1
    else:
        col = 2

    # return list with row and collumn values
    return [row, col]


# Return current square value from grid

def get_square_val(square, grid):
    val = get_square(square)
    return grid[val[0]][val[1]]

# Set value by square to player


def place_score(player, square, grid):
    val = get_square(square)
    grid[val[0]][val[1]] = player

# Check board for a winner
# "" = no win
# O or X for player win
# T for tie game


def test_win(grid):

    # Check if player x won
    player = "X"
    player = test_win_player(grid, player)

    # If player X did not win check player O
    if player == "":
        player = "O"
        player = test_win_player(grid, player)

    # If neither player won check for Tie
    if player == "":
        if tie_game(grid):
            # Tie Game
            return "T"

    return player

# Check if player had won by player


def test_win_player(grid, player):

    # Check for row and collumn wins
    for i in range(3):
        count_col = 0
        count_row = 0
        for j in range(3):
            if grid[i][j] == player:
                count_row += 1
            if grid[j][i] == player:
                count_col += 1
        if count_col == 3 or count_row == 3:
            return player

    # Check for diagonal wins
    if get_square_val(1, grid) == player and get_square_val(5, grid) == player and get_square_val(9, grid) == player:
        return player
    if get_square_val(3, grid) == player and get_square_val(5, grid) == player and get_square_val(7, grid) == player:
        return player

    return ""

# Test for a tie game
# Retruns True or False


def tie_game(grid):
    for i in range(3):
        for j in range(3):
            # If any square is not X or O return false
            if grid[i][j] != "X" or grid[i][j] != "O":
                return False

    return True

# Prompt user to enter with a question
# Loops until yes or no entered
# Returns true or false


def yes_no_input(prompt):

    while(True):
        response = input(f"{prompt} (yes/no): ")
        response = response.lower()

        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Invalid Entry")


# Begin Code. Only run program if ran dirrectly
# not from another file such as test
if __name__ == "__main__":
    main()
