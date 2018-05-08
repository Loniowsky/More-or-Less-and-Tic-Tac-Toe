from abc import ABCMeta, abstractmethod

class AbstractState(metaclass=ABCMeta):
	@abstractmethod
	def recv_data(self, server_fsm):
		return True

class Wait_for_connect(AbstractState):
	#used to connect first player
	def recv_data(self, server_fsm):
		server_fsm.make_connection()
		server_fsm.state = Connected()
		return True

class Wait_for_connect2(AbstractState):
	#used to connect second player
	def recv_data(self, server_fsm):
		server_fsm.make_connection2()
		server_fsm.state = Connected()
		return True

class Connected(AbstractState):
	def recv_data(self, server_fsm):
		if server_fsm.select_game():
			server_fsm.state = Game()
		else:
			server_fsm.state = Wait_for_connect2()
		return True

class Game(AbstractState):
	def recv_data(self, server_fsm):
		server_fsm.start_game()
		server_fsm.state=Make_disconnect()
		return True

class Make_disconnect(AbstractState):
	def recv_data(self, server_fsm):
		server_fsm.make_disconnect()
		server_fsm.state=Wait_for_connect()
		return False
