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
            self.assertEqual(chess.Rook(chess.WHITE), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['a', 'h'], [8]):
            self.assertEqual(chess.Rook(chess.BLACK), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['b', 'g'], [1]):
            self.assertEqual(chess.Knight(chess.WHITE), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['b', 'g'], [8]):
            self.assertEqual(chess.Knight(chess.BLACK), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['c', 'f'], [1]):
            self.assertEqual(chess.Bishop(chess.WHITE), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(['c', 'f'], [8]):
            self.assertEqual(chess.Bishop(chess.BLACK), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(board.files, [2]):
            self.assertEqual(chess.Pawn(chess.WHITE), board.get_piece_at_position(file, rank))
        for file, rank in itertools.product(board.files, [7]):
            self.assertEqual(chess.Pawn(chess.BLACK), board.get_piece_at_position(file, rank))
        self.assertEqual(chess.Queen(chess.WHITE), board.get_piece_at_position('d', 1))
        self.assertEqual(chess.Queen(chess.BLACK), board.get_piece_at_position('d', 8))
        self.assertEqual(chess.King(chess.WHITE), board.get_piece_at_position('e', 1))
        self.assertEqual(chess.King(chess.BLACK), board.get_piece_at_position('e', 8))

if __name__ == '__main__':
    unittest.main()



    
