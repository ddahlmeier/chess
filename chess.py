import itertools


EMPTYCELL = "."
ROOK = "R"
KNIGHT = "N"
BISHOP = "B"
PAWN = "P"
KING = "K"
QUEEN = "Q"
WHITE = "W"
BLACK = "B"

class Board(object):
    """
    Class representing a chess board and position of all pieces using standard algebraic notation
    https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
    """

    def __init__(self):
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        self.files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.file_idx = dict(zip(self.files, range(len(self.files))))
        self.board = [[EMPTYCELL]*8 for _ in range(8)] 

    def file_to_idx(self, file):
        return self.file_idx[file]

    def get_piece_at_position(self, file, rank):
        """return piece at specified position or EMPTYCELL if cell is empty"""
        if file not in self.files or rank not in self.ranks:
            raise ValueError("Invalid board position %s %d" % (file, rank))
        return self.board[self.file_to_idx(file)][rank-1]

    def set_piece_at_position(self, file, rank, piece):
        """set piece at specified position"""
        if file not in self.files or rank not in self.ranks:
            raise ValueError("Invalid board position %s %d" % (file, rank))
        self.board[self.file_to_idx(file)][rank-1] = piece

    def init_pieces(self):
        """Initialize board with pieces at the initial starting position of the game"""
        for file, rank in [('a',1), ('a', 8), ('h', 1), ('h', 8)]:
            self.set_piece_at_position(file, rank, Rook(WHITE) if rank == 1 else Rook(BLACK))
        for file, rank in [('b',1), ('b', 8), ('g', 1), ('g', 8)]:
            self.set_piece_at_position(file, rank, Knight(WHITE) if rank == 1 else Knight(BLACK))
        for file, rank in [('c',1), ('c', 8), ('f', 1), ('f', 8)]:
            self.set_piece_at_position(file, rank, Bishop(WHITE) if rank == 1 else Bishop(BLACK))
        for file, rank in itertools.product(self.files, [2, 7]):
            self.set_piece_at_position(file, rank, Pawn(WHITE) if rank == 2 else Pawn(BLACK))
        self.set_piece_at_position('d', 1, Queen(WHITE))
        self.set_piece_at_position('d', 8, Queen(BLACK))
        self.set_piece_at_position('e', 1, King(WHITE))
        self.set_piece_at_position('e', 8, King(BLACK))

    def __str__(self):
        return '\n'.join([''.join(['{:2}'.format(str(self.get_piece_at_position(file, rank))) 
                                   for file in self.files]) for rank in self.ranks])


class Piece(object):
    """
    Class representing a chess piece
    """
    
    def __init__(self, color):
        self.color = color


class King(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "\u2654" if self.color == WHITE else "\u265A"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False
    

class Queen(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "\u2655" if self.color == WHITE else "\u265B"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    
class Rook(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "\u2656" if self.color == WHITE else "\u265C"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False


class Bishop(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "\u2657" if self.color == WHITE else "\u265D"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False


class Knight(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "\u2658" if self.color == WHITE else "\u265E"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False


class Pawn(Piece):

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "\u2659" if self.color == WHITE else "\u265F"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False
