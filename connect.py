import socket
import pickle

class Connect:

	TCP_IP = "127.0.0.1"
	TCP_PORT = 5005
	sockt = None
	conn = None
	addr = None
	__BUFFER_SIZE__ = 1024

	def __init__(self):
		self.sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sockt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sockt.bind((self.TCP_IP, self.TCP_PORT))
		self.sockt.listen(1)

	def make_connection(self):
		conn, addr =  self.sockt.accept()
		self.conn=conn
		self.addr=addr
		print("Connection successful, address = {}".format(self.addr))
		self.sockt.close()

	def send_data(self, data, if_receive):
		to_send_list = [if_receive]
		to_send_list.append(data)
		to_send = pickle.dumps(to_send_list)
		self.conn.send(to_send)
		recv = self.conn.recv(self.__BUFFER_SIZE__)
		if if_receive:
			return pickle.loads(recv)
		else:
			return

	def close_connection(self):
		to_send = pickle.dumps([False,'closed'])
		self.conn.send(to_send)
		self.conn.recv(self.__BUFFER_SIZE__)
		self.conn.close()