"""
Task 6: TicTacToe
"""

# Task 6.2: Custom exception class that inherits from Exception
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


# Task 6.3: Board class for TicTacToe game
class Board:
    valid_moves = ["upper left", "upper center", "upper right", 
                   "middle left", "center", "middle right", 
                   "lower left", "lower center", "lower right"]
    
    def __init__(self):
        # Create 3x3 board filled with spaces
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        # Initialize turn to X (X goes first)
        self.turn = "X"
    
    # Task 6.4: String representation of board
    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)
    
    # Task 6.5: Move method with validation and exception handling
    def move(self, move_string):
        # Check if move is valid
        if not move_string in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        
        # Convert move string to board coordinates
        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3  # row (0, 1, or 2)
        column = move_index % 3  # column (0, 1, or 2)
        
        # Check if spot is already taken
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")
        
        # Make the move
        self.board_array[row][column] = self.turn
        
        # Switch turns
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"
    
    # Task 6.6: Check game status method
    def whats_next(self):
        # Check if board is full (Cat's Game)
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            else:
                continue
            break
        
        if cat:
            return (True, "Cat's Game.")
        
        win = False
        
        # Check rows
        for i in range(3):
            if self.board_array[i][0] != " ":
                if (self.board_array[i][0] == self.board_array[i][1] and 
                    self.board_array[i][1] == self.board_array[i][2]):
                    win = True
                    break
        
        # Check columns
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " ":
                    if (self.board_array[0][i] == self.board_array[1][i] and 
                        self.board_array[1][i] == self.board_array[2][i]):
                        win = True
                        break
        
        # Check diagonals
        if not win:
            if self.board_array[1][1] != " ":  # center must be filled
                # Main diagonal (top-left to bottom-right)
                if (self.board_array[0][0] == self.board_array[1][1] and 
                    self.board_array[2][2] == self.board_array[1][1]):
                    win = True
                # Anti-diagonal (top-right to bottom-left)
                if (self.board_array[0][2] == self.board_array[1][1] and 
                    self.board_array[2][0] == self.board_array[1][1]):
                    win = True
        
        # Return game status
        if not win:
            if self.turn == "X":
                return (False, "X's turn.")
            else:
                return (False, "O's turn.")
        else:
            # Someone won - since turn switched, previous player won
            if self.turn == "O":
                return (True, "X wins!")
            else:
                return (True, "O wins!")


# Task 6.7: Main game implementation
def play_tictactoe():
    board = Board()
    
    print("Welcome to TicTacToe!")
    print("Valid moves:", ", ".join(Board.valid_moves))
    print("\n" + "=" * 40)
    
    while True:
        print(board)
        
        game_over, message = board.whats_next()
        
        if game_over:
            print("🎉 " + message)
            break
        
        print(f"\n{message}")
        move = input("Enter your move: ").strip().lower()
        
        try:
            board.move(move)
            print("\n" + "-" * 30)
        except TictactoeException as e:
            print(f"Error: {e.message}")
            print("Please try again.\n")


# Task 6.8: Test the program
if __name__ == "__main__":
    while True:
        play_tictactoe()
        
        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("Thanks for playing!")
            break
        print("\n" + "=" * 50)