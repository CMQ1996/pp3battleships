import random

"""
Battleships Game

A simple command-line Battleships game built in Python to demonstrate the use
of lists, loops, functions, and input validation.

The game creates a 5x10 grid and randomly places a single battleship.

The player must guess the location of the battleship by entering row and
column coordinates. After each guess, feedback is given and the board updates.

The game continues until the player sinks the battleship.
"""

board = [[0 for _ in range(10)] for _ in range(5)]


def print_board(board):
    """
    Display the current game board in a readable grid format.

    Each cell represents:
    - 0: Unexplored position
    - X: Missed guess
    - S: Ship location (revealed when hit)
    """
    for row in board:
        print(" ".join(str(cell) for cell in row))


def random_row(board_grid):
    """Generate a random valid row index based on board size."""
    return random.randint(0, len(board_grid) - 1)


def random_col(board_grid):
    """Generate a random valid column index based on board size."""
    return random.randint(0, len(board_grid[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print("Let's play Battleships!")
print_board(board)

print("\nTry to sink my battleship!")

while True:
    """ Get validated row guess """
    while True:
        try:
            guess_row = int(input("\nGuess row (0-4): "))
            if 0 <= guess_row <= 4:
                break
            print("Row must be between 0 and 4!")
        except ValueError:
            print("Please enter a valid number!")

    """ Get validated column guess """
    while True:
        try:
            guess_col = int(input("Guess col (0-9): "))
            if 0 <= guess_col <= 9:
                break
            print("Column must be between 0 and 9!")
        except ValueError:
            print("Please enter a valid number!")

    """ Check hit or miss """
    if guess_row == ship_row and guess_col == ship_col:
        print("\n🎉 Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "S"
        break

    print("You missed my battleship!")
    board[guess_row][guess_col] = "X"

    print_board(board)

print("\nFinal board:")
print_board(board)
