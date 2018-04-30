from unittest import TestCase

from tictactoe.validators.input_validator import name_validation, move_validation



class TestValidator(TestCase):
    def test_if_win_returns_true_when_name_valid(self):
        name = "Janusz"
        self.assertEqual(name_validation(name), True)

    def test_if_win_returns_true_when_name_valid2(self):
        name = "Asdohgasg"
        self.assertEqual(name_validation(name), True)

    def test_if_win_returns_true_when_name_valid3(self):
        name = "ASGHWqwgqwQWgh"
        self.assertEqual(name_validation(name), True)

    def test_if_win_returns_true_when_name_invalid(self):
        name = "asssssssss"
        self.assertEqual(name_validation(name), False)

    def test_if_win_returns_true_when_name_invalid2(self):
        name = " "
        self.assertEqual(name_validation(name), False)

    def test_if_win_returns_true_when_name_invalid3(self):
        name = "----asdK"
        self.assertEqual(name_validation(name), False)

    def test_if_win_returns_true_when_name_invalid4(self):
        name = "Akakakaksdksadksakgkaskgk"
        self.assertEqual(name_validation(name), False)

    def test_if_move_returns_true_when_valid(self):
        input = 0
        self.assertEqual(move_validation(input), True)

    def test_if_move_returns_true_when_valid2(self):
        input = 3
        self.assertEqual(move_validation(input), True)

    def test_if_move_returns_true_when_valid3(self):
        input = 21536523
        self.assertEqual(move_validation(input), True)

    def test_if_move_returns_true_when_valid4(self):
        input = "94"
        self.assertEqual(move_validation(input), True)

    def test_if_move_returns_false_when_invalid(self):
        input = -4
        self.assertEqual(move_validation(input), False)

    def test_if_move_returns_false_when_invalid2(self):
        input = "asdasdasdsd"
        self.assertEqual(move_validation(input), False)

    def test_if_move_returns_false_when_invalid3(self):
        input = "assssssdasds"
        self.assertEqual(move_validation(input), False)