import socket 

def MakeServerSocket(host='', port=8888, limit=10):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	try:
		s.bind((host, port)) 
	except socket.error as msg: 
		print('bind fails: '+str(msg[0])) 
		import sys
		sys.exit(-1)
	s.listen(limit) 
	return s
	
	
s = MakeServerSocket()
while True:
	conn, addr = s.accept()
	conn.sendall(bytes(5))

	

	
