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
        self.pieces = set()

    def file_to_idx(self, file):
        return self.file_idx[file]

    def get_piece_at_position(self, file, rank):
        """return piece at specified position or EMPTYCELL if cell is empty"""
        if file not in self.files or rank not in self.ranks:
            raise ValueError("Invalid board position %s %d" % (file, rank))
        return self.board[self.file_to_idx(file)][rank-1]

    def set_piece(self, piece):
        """set piece at specified position"""
        self.board[self.file_to_idx(piece.file)][piece.rank-1] = piece
        self.pieces.add(piece)

    def is_empty(self, file, rank):
        """helper function to check if cell is empty"""
        return self.get_piece_at_position(file, rank) == EMPTYCELL

    def clear_board(self):
        """clear all pieces to create empty board"""
        self.board = [[EMPTYCELL]*8 for _ in range(8)] 
        for piece in self.pieces:
            piece.board = None

    def init_pieces(self):
        """Initialize board with pieces at the initial starting position of the game"""
        for file, rank in [('a',1), ('a', 8), ('h', 1), ('h', 8)]:
            self.set_piece(Rook(file, rank, WHITE, self) if rank == 1 else Rook(file, rank, BLACK, self))
        for file, rank in [('b',1), ('b', 8), ('g', 1), ('g', 8)]:
            self.set_piece(Knight(file, rank, WHITE, self) if rank == 1 else Knight(file, rank, BLACK, self))
        for file, rank in [('c',1), ('c', 8), ('f', 1), ('f', 8)]:
            self.set_piece(Bishop(file, rank, WHITE, self) if rank == 1 else Bishop(file, rank, BLACK, self))
        for file, rank in itertools.product(self.files, [2, 7]):
            self.set_piece(Pawn(file, rank, WHITE, self) if rank == 2 else Pawn(file, rank, BLACK, self))
        self.set_piece(Queen('d', 1, WHITE, self))
        self.set_piece(Queen('d', 8, BLACK, self))
        self.set_piece(King('e', 1, WHITE, self))
        self.set_piece(King('e', 8, BLACK, self))

    def __str__(self):
        return '  ' + ''.join(['{:2}'.format(file) for file in self.files]) + '\n' +  \
            '\n'.join([ '{:2}'.format(rank) + 
                        ''.join(['{:2}'.format(str(self.get_piece_at_position(file, rank))) for file in self.files]) 
                        + '{:2}'.format(rank) 
                        for rank in reversed(self.ranks)]) + \
                        '\n  ' + ''.join(['{:2}'.format(file) for file in self.files])


class Piece(object):
    """
    Class representing a chess piece
    """
    
    def __init__(self, file, rank, board):
        if file not in board.files or rank not in board.ranks:
            raise ValueError("Invalid board position %s %d" % (file, rank))
        self.file = file
        self.rank = rank
        self.board = board


class King(Piece):

    def __init__(self, file, rank, color, board):
        super(King, self).__init__(file, rank, board)
        self.color = color

    def __str__(self):
        return "\u2654" if self.color == WHITE else "\u265A"

    def __eq__(self, other):
        # TODO: are pieces only equal when their positon is equal?
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    def __hash__(self):
        return hash(self.file) ^ hash(self.rank) ^ hash(self.color) ^ hash(KING)
    

class Queen(Piece):

    def __init__(self, file, rank, color, board):
        super(Queen, self).__init__(file, rank, board)
        self.color = color

    def __str__(self):
        return "\u2655" if self.color == WHITE else "\u265B"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    def __hash__(self):
        return hash(self.file) ^ hash(self.rank) ^ hash(self.color) ^ hash(QUEEN)

    
class Rook(Piece):

    def __init__(self, file, rank, color, board):
        super(Rook, self).__init__(file, rank, board)
        self.color = color

    def valid_moves(self):
        moves = set()
        directions = [[(self.file, rank) for rank in range(self.rank-1, 0, -1)],
                      [(self.file, rank) for rank in range(self.rank+1, 9)],
                      [(file, self.rank) for file in self.board.files[(self.board.file_to_idx(self.file)+1):]],
                      [(file, self.rank) for file in reversed(self.board.files[:self.board.file_to_idx(self.file)])]]
        for direction in directions:
            for file, rank in direction:
                if self.board.is_empty(file, rank):
                    moves.add((file, rank))
                else:
                    break
        return moves

    def __str__(self):
        return "\u2656" if self.color == WHITE else "\u265C"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    def __hash__(self):
        return hash(self.file) ^ hash(self.rank) ^ hash(self.color) ^ hash(ROOK)


class Bishop(Piece):

    def __init__(self, file, rank, color, board):
        super(Bishop, self).__init__(file, rank, board)
        self.color = color

    def valid_moves(self):
        moves = set()
        file_left = list(reversed(self.board.files[:self.board.file_to_idx(self.file)]))
        file_right = self.board.files[(self.board.file_to_idx(self.file)+1):]
        rank_bottom = list(range(self.rank-1, 0, -1))
        rank_top = list(range(self.rank+1, 9))
        directions = [ zip(file_left, rank_bottom),
                       zip(file_left, rank_top),
                       zip(file_right, rank_bottom),
                       zip(file_right, rank_top)]
        for direction in directions:
            for file, rank in direction:
                if self.board.is_empty(file, rank):
                    moves.add((file, rank))
                else:
                    break
        return moves

    def __str__(self):
        return "\u2657" if self.color == WHITE else "\u265D"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    def __hash__(self):
        return hash(self.file) ^ hash(self.rank) ^ hash(self.color) ^ hash(BISHOP)


class Knight(Piece):

    def __init__(self, file, rank, color, board):
        super(Knight, self).__init__(file, rank, board)
        self.color = color

    def __str__(self):
        return "\u2658" if self.color == WHITE else "\u265E"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    def __hash__(self):
        return hash(self.file) ^ hash(self.rank) ^ hash(self.color) ^ hash(KNIGHT)


class Pawn(Piece):

    def __init__(self, file, rank, color, board):
        super(Pawn, self).__init__(file, rank, board)
        self.color = color

    def valid_moves(self):
        moves = []
        if self.color == WHITE:
            if self.board.is_empty(self.file, self.rank+1):
                moves.append((self.file, self.rank+1))
                if self.rank == 2 and self.board.is_empty(self.file, self.rank+2):
                    moves.append((self.file, self.rank+2))
        elif self.color == BLACK:
            if self.board.is_empty(self.file, self.rank-1):
                moves.append((self.file, self.rank-1))
                if self.rank == 7 and self.board.is_empty(self.file, self.rank-2):
                    moves.append((self.file, self.rank-2))
        else:
            assert False
        return moves

    def __str__(self):
        return "\u2659" if self.color == WHITE else "\u265F"

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.color == other.color
        return False

    def __hash__(self):
        return hash(self.file) ^ hash(self.rank) ^ hash(self.color) ^ hash(PAWN)
