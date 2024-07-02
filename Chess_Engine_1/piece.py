class Piece:
    def __init__(self, color, row, col) -> None:
        self.color = color
        self.row = row
        self.col = col
        pass
    def possible_moves(self, board):
        raise NotImplementedError
    def is_within_board(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
    
class Pawn(Piece):
    def possible_moves(self, board, last_move):
        direction = -1 if self.color == "white" else 1
        start_row = 6 if self.color == "white" else 1
        enemy_color = "black" if self.color == "white" else "white"
        moves = []

        # Move one step forward
        if self.is_within_board(self.row + direction, self.col) and board[self.row + direction][self.col] is None:
            moves.append([self.row + direction, self.col])
            # Move two steps forward from the starting position
            if self.row == start_row and board[self.row + 2 * direction][self.col] is None:
                moves.append([self.row + 2 * direction, self.col])
        
        # Capture diagonally
        for offset in [-1, 1]:
            if self.is_within_board(self.row + direction, self.col + offset) and board[self.row + direction][self.col + offset] is not None:
                if board[self.row + direction][self.col + offset].color == enemy_color:
                    moves.append([self.row + direction, self.col + offset])
        # En Passant
        if last_move and isinstance(last_move.piece, Pawn):
            if abs(last_move.start_row - last_move.end_row) == 2 and last_move.end_row == self.row:
                for offset in [-1, 1]:
                    if self.is_within_board(self.row, self.col + offset) and self.col + offset == last_move.end_col:
                        if board[self.row][self.col + offset] is not None and board[self.row][self.col + offset].color == enemy_color:
                            moves.append([self.row + direction, self.col + offset])
            
        
        

        return moves
    def draw_piece(self, screen, images):
        piece_name = f'{self.color}_pawn'
        image = images[piece_name]
        screen.blit(image, (self.col*60, self.row*60))

class Bishop(Piece):
    def possible_moves(self, board):
        #possible moves for pawn
        pass
    def draw_piece(self, screen, images):
        piece_name = f'{self.color}_bishop'
        image = images[piece_name]
        screen.blit(image, (self.col*60, self.row*60))

class Knight(Piece):
    def possible_moves(self, board):
        #possible moves for pawn
        pass
    def draw_piece(self, screen, images):
        piece_name = f'{self.color}_knight'
        image = images[piece_name]
        screen.blit(image, (self.col*60, self.row*60))

class Rook(Piece):
    def possible_moves(self, board):
        #possible moves for pawn
        pass
    def draw_piece(self, screen, images):
        piece_name = f'{self.color}_rook'
        image = images[piece_name]
        screen.blit(image, (self.col*60, self.row*60))

class Queen(Piece):
    def possible_moves(self, board):
        #possible moves for pawn
        pass
    def draw_piece(self, screen, images):
        piece_name = f'{self.color}_queen'
        image = images[piece_name]
        screen.blit(image, (self.col*60, self.row*60))

class King(Piece):
    def possible_moves(self, board):
        #possible moves for pawn
        pass
    def draw_piece(self, screen, images):
        piece_name = f'{self.color}_king'
        image = images[piece_name]
        screen.blit(image, (self.col*60, self.row*60))