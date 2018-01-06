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
        board.init_pieces()
        pawn = chess.Pawn('a', 3, chess.WHITE, board)
        board.set_piece(pawn)
        self.assertEqual([('a', 4)],  pawn.valid_moves())
        
    def test_black_pawn_can_move_forward_by_one(self):
        board = chess.Board()
        board.init_pieces()
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
        board.init_pieces()
        pawn = chess.Pawn('a', 7, chess.BLACK, board)
        board.set_piece(pawn)
        self.assertEqual([('a', 6), ('a', 5)],  pawn.valid_moves())

if __name__ == '__main__':
    unittest.main()



    
