import itertools
import unittest

import chess


class InitGameTest(unittest.TestCase):

    def test_create_empty_board(self):
        board = chess.Board()
        self.assertTrue(all(board.get_piece_at_position(file, rank) == chess.EMPTYCELL
                       for file in board.files for rank in board.ranks))

    def test_create_board_with_pieces(self):
        board = chess.Board()
        board.init_pieces()
        for file, rank in itertools.product(['a', 'h'], [1]):
            self.assertEqual(chess.Rook(file, rank, chess.WHITE, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['a', 'h'], [8]):
            self.assertEqual(chess.Rook(file, rank, chess.BLACK, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['b', 'g'], [1]):
            self.assertEqual(chess.Knight(file, rank, chess.WHITE, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['b', 'g'], [8]):
            self.assertEqual(chess.Knight(file, rank, chess.BLACK, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['c', 'f'], [1]):
            self.assertEqual(chess.Bishop(file, rank, chess.WHITE, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['c', 'f'], [8]):
            self.assertEqual(chess.Bishop(file, rank, chess.BLACK, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(board.files, [2]):
            self.assertEqual(chess.Pawn(file, rank, chess.WHITE, board), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(board.files, [7]):
            self.assertEqual(chess.Pawn(file, rank, chess.BLACK, board), board.get_piece_at_position(file, rank))
        self.assertEqual(chess.Queen('d', 1, chess.WHITE, board), board.get_piece_at_position('d', 1))
        self.assertEqual(chess.Queen('d', 8, chess.BLACK, board), board.get_piece_at_position('d', 8))
        self.assertEqual(chess.King('e', 1, chess.WHITE, board), board.get_piece_at_position('e', 1))
        self.assertEqual(chess.King('e', 8, chess.BLACK, board), board.get_piece_at_position('e', 8))
        for file, rank in itertools.product(board.files, [3,4,5,6]):
            self.assertTrue(board.is_empty(file, rank))

    def test_white_pawn_can_move_forward_by_one(self):
        board = chess.Board()
        pawn = chess.Pawn('a', 3, chess.WHITE, board)
        board.set_piece(pawn)
        self.assertEqual([('a', 4)],  pawn.valid_moves())
        
    def test_black_pawn_can_move_forward_by_one(self):
        board = chess.Board()
        pawn = chess.Pawn('a', 6, chess.BLACK, board)
        board.set_piece(pawn)
        self.assertEqual([('a', 5)],  pawn.valid_moves())

    def test_white_pawn_can_move_forward_by_one_or_two(self):
        board = chess.Board()
        board.init_pieces()
        pawn = chess.Pawn('a', 2, chess.WHITE, board)
        board.set_piece(pawn)
        self.assertEqual([('a', 3), ('a', 4)],  pawn.valid_moves())
        
    def test_black_pawn_can_move_forward_by_one_or_two(self):
        board = chess.Board()
        pawn = chess.Pawn('a', 7, chess.BLACK, board)
        board.set_piece(pawn)
        self.assertEqual([('a', 6), ('a', 5)],  pawn.valid_moves())

    def test_rook_can_move(self):
        board = chess.Board()
        rook_white = chess.Rook('d', 4, chess.WHITE, board)
        true_moves = set([('a', 4), ('b', 4), ('c', 4), ('e', 4), ('f', 4), \
                              ('g', 4), ('h', 4), ('d', 1), ('d', 2), ('d', 3), \
                              ('d', 5), ('d', 6), ('d', 7), ('d', 8)])
        board.set_piece(rook_white)
        self.assertEqual(true_moves, rook_white.valid_moves())
        rook_black = chess.Rook('d', 4, chess.BLACK, board)
        board.set_piece(rook_black)
        self.assertEqual(true_moves, rook_black.valid_moves())

    def test_rook_canot_move_through_other_pieces(self):
        board = chess.Board()
        rook = chess.Rook('d', 4, chess.WHITE, board)
        board.set_piece(rook)
        self.assertEqual(set([('a', 4), ('b', 4), ('c', 4), ('e', 4), ('f', 4), \
                              ('g', 4), ('h', 4), ('d', 1), ('d', 2), ('d', 3), \
                              ('d', 5), ('d', 6), ('d', 7), ('d', 8)]), rook.valid_moves())
        board.set_piece(chess.Rook('d', 5, chess.WHITE, board))
        self.assertEqual(set([('a', 4), ('b', 4), ('c', 4), ('e', 4), ('f', 4), \
                                  ('g', 4), ('h', 4), ('d', 1), ('d', 2), ('d', 3)]), \
                             rook.valid_moves())
        board.set_piece(chess.Rook('d', 3, chess.WHITE, board))
        self.assertEqual(set([('a', 4), ('b', 4), ('c', 4), ('e', 4), ('f', 4), \
                                  ('g', 4), ('h', 4)]), \
                             rook.valid_moves())
        board.set_piece(chess.Rook('c', 4, chess.WHITE, board))
        self.assertEqual(set([('e', 4), ('f', 4), ('g', 4), ('h', 4)]), \
                             rook.valid_moves())
        board.set_piece(chess.Rook('e', 4, chess.WHITE, board))
        self.assertEqual(set(), rook.valid_moves())

    def test_bishop_can_move(self):
        board = chess.Board()
        bishop_white = chess.Bishop('d', 4, chess.WHITE, board)
        true_moves = set([('a', 7), ('b', 6), ('c', 5), ('e', 3), ('f', 2), ('g', 1), \
                              ('a', 1), ('b', 2), ('c', 3), ('e', 5), ('f', 6), ('g', 7), ('h', 8)])
        board.set_piece(bishop_white)
        self.assertEqual(true_moves, bishop_white.valid_moves())
        bishop_black = chess.Bishop('d', 4, chess.BLACK, board)
        board.set_piece(bishop_black)
        self.assertEqual(true_moves, bishop_black.valid_moves())

    def test_bishop_canot_move_through_other_pieces(self):
        board = chess.Board()
        bishop = chess.Bishop('d', 4, chess.WHITE, board)
        board.set_piece(bishop)
        self.assertEqual(set([('a', 7), ('b', 6), ('c', 5), ('e', 3), ('f', 2), ('g', 1), \
                              ('a', 1), ('b', 2), ('c', 3), ('e', 5), ('f', 6), ('g', 7), \
                                  ('h', 8)]), bishop.valid_moves())
        board.set_piece(chess.Bishop('c', 3, chess.WHITE, board))
        self.assertEqual(set([('a', 7), ('b', 6), ('c', 5), ('e', 3), ('f', 2), ('g', 1), \
                                  ('e', 5), ('f', 6), ('g', 7), ('h', 8)]), bishop.valid_moves())
        board.set_piece(chess.Bishop('c', 5, chess.WHITE, board))
        self.assertEqual(set([('e', 3), ('f', 2), ('g', 1), \
                                 ('e', 5), ('f', 6), ('g', 7), ('h', 8)]), bishop.valid_moves())
        board.set_piece(chess.Bishop('e', 5, chess.WHITE, board))
        self.assertEqual(set([('e', 3), ('f', 2), ('g', 1)]), bishop.valid_moves())
        board.set_piece(chess.Bishop('e', 3, chess.WHITE, board))
        self.assertEqual(set(), bishop.valid_moves())

    def test_knight_can_move(self):
        board = chess.Board()
        knight_white = chess.Knight('d', 4, chess.WHITE, board)
        true_moves = set([('e', 6), ('f', 5), ('f', 3), ('e', 2), ('c', 2), ('b', 3), ('b', 5), ('c', 6)])
        board.set_piece(knight_white)
        self.assertEqual(true_moves, knight_white.valid_moves())
        knight_black = chess.Knight('d', 4, chess.BLACK, board)
        board.set_piece(knight_black)
        self.assertEqual(true_moves, knight_black.valid_moves())

    def test_knight_cannot_move_to_occupied_cell(self):
        board = chess.Board()
        knight_white = chess.Knight('d', 4, chess.WHITE, board)
        pawn_white = chess.Pawn('c', 6, chess.WHITE, board)
        true_moves = set([('e', 6), ('f', 5), ('f', 3), ('e', 2), ('c', 2), ('b', 3), ('b', 5)])
        board.set_piece(knight_white)
        board.set_piece(pawn_white)
        self.assertEqual(true_moves, knight_white.valid_moves())

    def test_queen_can_move(self):
        board = chess.Board()
        queen_white = chess.Queen('d', 4, chess.WHITE, board)
        rook_moves = set([('a', 4), ('b', 4), ('c', 4), ('e', 4), ('f', 4), \
                              ('g', 4), ('h', 4), ('d', 1), ('d', 2), ('d', 3), \
                              ('d', 5), ('d', 6), ('d', 7), ('d', 8)])
        bishop_moves = set([('a', 7), ('b', 6), ('c', 5), ('e', 3), ('f', 2), ('g', 1), \
                              ('a', 1), ('b', 2), ('c', 3), ('e', 5), ('f', 6), ('g', 7), ('h', 8)])
        true_moves = rook_moves.union(bishop_moves)
        board.set_piece(queen_white)
        self.assertEqual(true_moves, queen_white.valid_moves())

    def test_king_can_move(self):
        board = chess.Board()
        king_white = chess.King('d', 4, chess.WHITE, board)
        true_moves = set([('d',3), ('d',5), ('c',4), ('e',4), ('c',3), ('c',5), ('e',3), ('e',5)]) 
        board.set_piece(king_white)
        self.assertEqual(true_moves, king_white.valid_moves())

    def test_king_cannot_move_to_occupied_cell(self):
        board = chess.Board()
        king_white = chess.King('d', 4, chess.WHITE, board)
        pawn_white = chess.Pawn('d', 3, chess.WHITE, board)
        true_moves = set([('d',5), ('c',4), ('e',4), ('c',3), ('c',5), ('e',3), ('e',5)]) 
        board.set_piece(king_white)
        board.set_piece(pawn_white)
        self.assertEqual(true_moves, king_white.valid_moves())


if __name__ == '__main__':
    unittest.main()



    
