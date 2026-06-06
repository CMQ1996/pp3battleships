import random

"""
Battleships Game
This project is a simple battleships game written with python to demonstrate the use of lists, loops, and input validation. The game creates a 5x10 grid where a single battleship is randomly placed. The player must guess the location of the battleship by entering row and column numbers. The game provides feedback on whether the guess was a hit or a miss, and updates the board accordingly. The game continues until the player successfully sinks the battleship.
"""

board = [[0 for _ in range(10)] for _ in range(5)]


def print_board(board):
    """
    Prints the game board in a readable grid format.
    Each cell shows either:
    - 0 for empty
    - X for a miss
    - S for the ship (when revealed)
    """
    for row in board:
        print(" ".join(str(cell) for cell in row))


def random_row(board_grid):
    """
    Returns a random valid row index based on the board size.
    """
    return random.randint(0, len(board_grid) - 1)


def random_col(board_grid):
    """
    Returns a random valid column index based on the board size.
    """
    return random.randint(0, len(board_grid[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


"""
Game start message and initial board display.
"""
print("Let's play Battleships!")
print_board(board)

print("\nTry to sink my battleship!")


"""
Main game loop which enables the player to continue guessing until they find the ship. It includes input validation for both row and column guesses, and updates the board accordingly after each guess.
"""
while True:
    """Get validated row guess from the player.
    """
    while True:
        try:
            guess_row = int(input("\nGuess row (0-4): "))
            if 0 <= guess_row <= 4:
                break
            else:
                print("Row must be between 0 and 4!")
        except ValueError:
            print("Please enter a valid number!")

    """
    Get validated column guess from the player."""
    while True:
        try:
            guess_col = int(input("Guess col (0-9): "))
            if 0 <= guess_col <= 9:
                break
            else:
                print("Column must be between 0 and 9!")
        except ValueError:
            print("Please enter a valid number!")

    """
    Checks for hit or miss and updates the board accordingly. If the guess is correct, it marks the ship's location with 'S' and ends the game. If the guess is a miss, it marks the location with 'X' and continues the game.
    """
    if guess_row == ship_row and guess_col == ship_col:
        print("\n🎉 Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "S"
        break

    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"

    print_board(board)


"""
Final game state display after the loop ends.
"""
print("\nFinal board:")
print_board(board)