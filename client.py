import socket
import pickle

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1000

sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockt.connect((TCP_IP, TCP_PORT))
data = ''

while not data == "closed":
	rcv = sockt.recv(BUFFER_SIZE)
	data_list = pickle.loads(rcv)
	flag = data_list[0]
	data = data_list[1]
	if flag:
		to_send = input(data)
		sockt.send(pickle.dumps(to_send))
	else:
		print(data)
		sockt.send(pickle.dumps("ok"))