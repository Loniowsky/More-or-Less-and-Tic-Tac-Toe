from unittest import TestCase
from tictactoe.gameplay import Gameplay
from tictactoe.board import Board
from unittest.mock import patch


class TestGameplay(TestCase):

    def test_if_win_returns_true_when_win(self):
        test_gameplay = Gameplay()
        test_board = Board(3, 3)
        test_board.set_element(0, 0, 'o')
        test_board.set_element(0, 1, 'o')
        test_board.set_element(0, 2, 'x')
        test_board.set_element(1, 0, 'x')
        test_board.set_element(1, 1, 'x')
        test_board.set_element(1, 2, 'o')
        test_board.set_element(2, 0, 'x')
        test_board.set_element(2, 1, 'x')
        test_board.set_element(2, 2, 'x')

        test_gameplay.set_board(test_board)
        test_gameplay.set_win_limit(3)

        self.assertEqual(test_gameplay.is_win(), True)

    def test_if_win_returns_false_when_no_win(self):
        test_gameplay = Gameplay()
        test_board = Board(3, 3)
        test_board.set_element(0, 0, 'o')
        test_board.set_element(0, 1, 'o')
        test_board.set_element(0, 2, 'x')
        test_board.set_element(1, 0, 'x')
        test_board.set_element(1, 1, 'x')
        test_board.set_element(1, 2, 'o')
        test_board.set_element(2, 0, 'x')
        test_board.set_element(2, 1, 'x')
        test_board.set_element(2, 2, 'x')

        test_gameplay.set_board(test_board)
        test_gameplay.set_win_limit(4)

        self.assertEqual(test_gameplay.is_win(), False)


