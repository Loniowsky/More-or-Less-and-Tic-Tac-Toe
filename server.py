from connect import Connect
from tictactoe.Multiplayer.multi_gameplay import MultiplayerGameplay
from More_or_less.molgameplay import MoLGameplay
from state_machine import *

class ServerFSM:

	mode = ""
	def __init__(self):
		self.state = Wait_for_connect()

	def recv_data(self):
		return self.state.recv_data(self)

	def make_connection(self):
		print("make_connection")
		self.connection_one = Connect()
		self.connection_one.make_connection()
		
	def make_connection2(self):
		print("make_connection2")
		self.connection_two = Connect()
		self.connection_two.make_connection()
		

	def select_game(self):
		print("select_game")
		if not ( self.mode == "ttt" or self.mode == "mol" ):
			self.mode = self.connection_one.send_data("Choose game (mol - more or less OR ttt - Tic-Tac-Toe) :", True)
			if not (self.mode == "ttt" or self.mode == "mol"):
				self.mode = self.connection_one.send_data("Choose game (mol - more or less OR ttt - Tic-Tac-Toe) :", True)
			if self.mode == "mol":
				return True
			else:
				return False
		else:
			return True
		

	def start_game(self):
		print("start game")
		if self.mode == 'ttt':
			self.game = MultiplayerGameplay(self.connection_one, self.connection_two)
			self.game.start()
		else:
			self.game = MoLGameplay(self.connection_one)
			self.connection_two = False
			self.game.start()

	def make_disconnect(self):
		print("make disconnect")
		if self.connection_two:
			self.connection_two.close_connection()
		self.connection_one.close_connection()

class Server:
	def __init__(self):
		self.fsm = ServerFSM()
	def recv_data(self):
		return self.fsm.recv_data()

server = Server()
while server.recv_data():
	pass
	

		


# con1 = Connect()
# con1.make_connection()

# mode = con1.send_data("Choose game (mol - more or less OR ttt - Tic-Tac-Toe) :", True)
# if not (mode == "ttt" or mode == "mol"):
# 	mode = con1.send_data("Choose game (mol - more or less OR ttt - Tic-Tac-Toe) :", True)

# if mode == 'ttt':
#     con2 = Connect()
#     con2.make_connection()
#     gameplay = MultiplayerGameplay(con1, con2)
#     gameplay.start()
#     con2.close_connection()
#     con1.close_connection()

# if mode == "mol":
#     gameplay = MoLGameplay(con1)
#     gameplay.start()
#     con1.close_connection()

