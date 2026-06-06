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

"""
This code allows the player to take turns guessing the location of the ship.
"""
guess_row = int(input("guess row (0-4):"))
guess_col = int(input("guess col (0-9):"))

"""
This if else statement checks whether the plater hits the ship with their guess
"""
if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
else:
    print("You missed my battleship!")

"""
This if statement marks misses on the board.
"""
if guess_row != ship_row or guess_col != ship_col:
    board[guess_row][guess_col] = "X"
print_board(board)

