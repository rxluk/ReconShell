import socket
import sys

portas = [21, 22, 80, 443, 8080, 3306]
host =  sys.argv[1]

for porta in range(1, 65536):
	mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mySocket.settimeout(1)

	code = mySocket.connect_ex((host, porta))

	if(code == 0):
		mySocket.connect((host, porta))

		try:
			banner = mySocket.recv(1024).decode().replace("\n", "")
		except:
			banner = "Não identificado"

		print(porta, banner)
		mySocket.close()
