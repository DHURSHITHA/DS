class ChessGame:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.white_turn = True

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def get_pawn_moves(self, row, col):
        moves = []
        direction = -1 if self.board[row][col].isupper() else 1
        start_row = 6 if self.board[row][col].isupper() else 1

        # Move forward one square
        if self.board[row + direction][col] == ' ':
            moves.append((row + direction, col))

            # Move forward two squares from starting position
            if row == start_row and self.board[row + 2 * direction][col] == ' ':
                moves.append((row + 2 * direction, col))

        # Capture diagonally
        if col - 1 >= 0 and self.board[row + direction][col - 1] != ' ' and self.board[row + direction][col - 1].isupper() != self.white_turn:
            moves.append((row + direction, col - 1))
        if col + 1 < 8 and self.board[row + direction][col + 1] != ' ' and self.board[row + direction][col + 1].isupper() != self.white_turn:
            moves.append((row + direction, col + 1))

        return moves

    def get_rook_moves(self, row, col):
        # Placeholder for rook moves
        return []

    def get_knight_moves(self, row, col):
        # Placeholder for knight moves
        return []

    def get_bishop_moves(self, row, col):
        # Placeholder for bishop moves
        return []

    def get_queen_moves(self, row, col):
        # Placeholder for queen moves
        return []

    def get_king_moves(self, row, col):
        # Placeholder for king moves
        return []

    def get_piece_moves(self, row, col):
        piece = self.board[row][col].lower()
        if piece == 'p':
            return self.get_pawn_moves(row, col)
        elif piece == 'r':
            return self.get_rook_moves(row, col)
        elif piece == 'n':
            return self.get_knight_moves(row, col)
        elif piece == 'b':
            return self.get_bishop_moves(row, col)
        elif piece == 'q':
            return self.get_queen_moves(row, col)
        elif piece == 'k':
            return self.get_king_moves(row, col)
        else:
            return []

    def is_valid_move(self, row, col, new_row, new_col):
        # Check if the move is within the board boundaries
        if new_row < 0 or new_row >= 8 or new_col < 0 or new_col >= 8:
            return False
        # Check if the destination square is occupied by the same color
        if self.board[new_row][new_col] != ' ' and self.board[new_row][new_col].isupper() == self.white_turn:
            return False
        # Check if the move is legal for the piece
        piece_moves = self.get_piece_moves(row, col)
        return (new_row, new_col) in piece_moves

    def make_move(self, row, col, new_row, new_col):
        piece = self.board[row][col]
        self.board[row][col] = ' '
        self.board[new_row][new_col] = piece
        self.white_turn = not self.white_turn

    def play_game(self):
        while True:
            self.print_board()
            print("White's turn" if self.white_turn else "Black's turn")
            source = input("Enter the source square (e.g., a2): ")
            destination = input("Enter the destination square (e.g., a4): ")

            source_col = ord(source[0]) - ord('a')
            source_row = 8 - int(source[1])
            dest_col = ord(destination[0]) - ord('a')
            dest_row = 8 - int(destination[1])

            if self.is_valid_move(source_row, source_col, dest_row, dest_col):
                self.make_move(source_row, source_col, dest_row, dest_col)
            else:
                print("Invalid move. Please try again.")
                continue

# Start the game
game = ChessGame()
game.play_game()
output:
r n b q k b n r
p p p p p p p p
               
               
               
               
P P P P P P P P
R N B Q K B N R

White's turn
Enter the source square (e.g., a2): a2
Enter the destination square (e.g., a4): a4
r n b q k b n r
p p p p p p p p
               
               
P              
               
  P P P P P P P
R N B Q K B N R

Black's turn
Enter the source square (e.g., a2): 