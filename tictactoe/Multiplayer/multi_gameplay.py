import sys
sys.path.append('./tictactoe')
from gameplay import Gameplay
from board import Board
from player import Player
from validators.input_validator import move_validation, name_validation



class MultiplayerGameplay(Gameplay):
    Gameplay._win_limit = 3
    __player_one = Player()
    __player_two = Player()
    __BUFFER_SIZE = 1000

    def __init__(self, connection_one, connection_two, board_width=3, board_height=3, win_limit=3):
        self._board = Board(board_width, board_height)
        Gameplay._win_limit = win_limit
        for i in range(board_width):
            for j in range(board_height):
                self._board.set_element(i, j, '-')
        self.connection_one = connection_one
        self.connection_two = connection_two

        self.connection_two.send_data("Wait", False)
        while not self.is_player_name_valid(self.__player_one):
            data = self.connection_one.send_data("Write your name: ", True)
            print(name_validation(data))
            if name_validation(data):
                self.connection_one.send_data(self.set_player_name(data, 1), False)
        while not self.is_player_name_valid(self.__player_two):
            data = self.connection_two.send_data("Write your name: ", True)
            print(name_validation(data))
            if name_validation(data):
                self.connection_two.send_data(self.set_player_name(data, 2), False)

    def user_move(self, sign, player_socket):
        row = player_socket.send_data('Choode a row: ', True)
        while not move_validation(row):
            row = player_socket.send_data('Choode a row: ', True)
        row = int(row)

        column = player_socket.send_data('Choode a column: ', True)
        while not move_validation(column):
            column = player_socket.send_data('Choode a column: ', True)
        column = int(column)

        if self._is_not_out_of_board_range(row, column):
            self._board.set_element(row, column, sign)
        else:
            self.user_move(sign, player_socket)

    def start(self):
        while not self.is_win():
            self.connection_one.send_data(str(self._board), False)
            self.connection_one.send_data("{} turn! Your sign is: O".format(self.__player_one.get_name()), False)
            self.user_move('O', self.connection_one)
            self.connection_one.send_data(str(self._board), False)
            if self.is_win():
                self.connection_one.send_data(str(self._board), False)
                self.connection_two.send_data(str(self._board), False)
                break
            self.connection_two.send_data(str(self._board), False)
            self.connection_two.send_data("{} turn! Your sign is: O".format(self.__player_one.get_name()), False)
            self.user_move('X', self.connection_two)
            self.connection_two.send_data(str(self._board), False)
        self.connection_one.send_data(str(self._board), False)
        self.connection_two.send_data(str(self._board), False)

    def set_player_name(self, name, player):
        if player == 1:
            try:
                self.__player_one.set_name(name)
                return 'Name set.'
            except Exception as error:
                return error.message
        else:
            try:
                self.__player_two.set_name(name)
                return 'Name set.'
            except Exception as error:
                return error.message

    def is_player_name_valid(self, player):
        if player.is_name_empty():
            return False
        else:
            return True

