import random

"""
This is the requirements file for the Battleships game. It lists the dependencies needed to run the game.
"""
board = [[0 for _ in range(10)] for _ in range(5)]

"""
This function prints the game board in a readable format.
"""
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

"""
This code chooses a random position for a ship on the game board.
"""
def random_row(board_grid):
    return random.randint(0, len(board_grid) - 1)

def random_col(board_grid):
    return random.randint(0, len(board_grid[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

"""
This code shows the board to the player
"""
print("Let's play Battleships!")
print_board(board)

print("\nTry to sink my battleship!")

""""
This is the main game loop. It continues until the player sinks the ship.
"""
while True:
    # Get validated row guess
    while True:
        try:
            guess_row = int(input("\nGuess row (0-4): "))
            if 0 <= guess_row <= 4:
                break
            else:
                print("Row must be between 0 and 4!")
        except ValueError:
            print("Please enter a valid number!")

    # Get validated column guess
    while True:
        try:
            guess_col = int(input("Guess col (0-9): "))
            if 0 <= guess_col <= 9:
                break
            else:
                print("Column must be between 0 and 9!")
        except ValueError:
            print("Please enter a valid number!")

    # Check if the player hit the ship
    if guess_row == ship_row and guess_col == ship_col:
        print("\n🎉 Congratulations! You sank my battleship!")
        board[guess_row][guess_col] = "S"   # Show the ship
        break                                   # Stop the game

    else:
        # Miss
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"     # Mark the miss

    # Show updated board after every miss
    print_board(board)

# Show final board when game ends
print("\nFinal board:")