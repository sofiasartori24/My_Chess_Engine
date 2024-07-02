import piece
from piece import Pawn

class Move:
    def __init__(self, piece, start_row, end_row, start_col, end_col) -> None:
        self.piece = piece
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col

class Game:
    def __init__(self) -> None:
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()
        self.current_turn = "white"
        self.is_check = False
        self.is_check_mate = False
        self.is_draw = False
        self.last_move = None

    def move_piece(self, piece, row, col):
        if piece.color == self.current_turn:
            possible_moves = piece.possible_moves(self.board, self.last_move)
            if [row, col] in possible_moves:
                # En Passant
                if self.last_move is not None:
                    print(self.last_move.start_row, self.last_move.end_row)
                if isinstance(piece, Pawn) and col != piece.col and self.board[row][col] is None:
                    captured_pawn_row = row + (1 if piece.color == "white" else -1)
                    self.board[captured_pawn_row][col] = None

                self.last_move = Move(piece, piece.row, row, piece.col, col)
                
                # Update the board
                self.board[piece.row][piece.col] = None
                piece.row = row
                piece.col = col
                self.board[row][col] = piece
                
                self.current_turn = "black" if self.current_turn == "white" else "white"

    def setup_board(self):
        for row in range(8):
            for col in range(8):
                if row == 0:
                    if col == 0:
                        self.board[row][col] = piece.Rook("black", row, col) 
                    if col == 1:
                        self.board[row][col] = piece.Knight("black", row, col) 
                    if col == 2:
                        self.board[row][col] = piece.Bishop("black", row, col) 
                    if col == 3:
                        self.board[row][col] = piece.Queen("black", row, col) 
                    if col == 4:
                        self.board[row][col] = piece.King("black", row, col) 
                    if col == 5:
                        self.board[row][col] = piece.Bishop("black", row, col) 
                    if col == 6:
                        self.board[row][col] = piece.Knight("black", row, col) 
                    if col == 7:
                        self.board[row][col] = piece.Rook("black", row, col) 
                if row == 1:
                    self.board[row][col] = piece.Pawn("black", row, col) 
                if row == 6:
                    self.board[row][col] = piece.Pawn("white", row, col) 
                if row == 7:
                    if col == 0:
                        self.board[row][col] = piece.Rook("white", row, col) 
                    if col == 1:
                        self.board[row][col] = piece.Knight("white", row, col) 
                    if col == 2:
                        self.board[row][col] = piece.Bishop("white", row, col) 
                    if col == 3:
                        self.board[row][col] = piece.Queen("white", row, col) 
                    if col == 4:
                        self.board[row][col] = piece.King("white", row, col) 
                    if col == 5:
                        self.board[row][col] = piece.Bishop("white", row, col) 
                    if col == 6:
                        self.board[row][col] = piece.Knight("white", row, col) 
                    if col == 7:
                        self.board[row][col] = piece.Rook("white", row, col) 