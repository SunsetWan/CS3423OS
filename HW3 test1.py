import socket

def YieldBST(T):
	if type(T) is not tuple:
		if T is not None:
			yield T
	else:
		yield from YieldBST(T[1])
		yield from YieldBST(T[0])
		yield from YieldBST(T[2])


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
	
conn, addr = s.accept()

L = []
T = (17,(12,(6,None,None),(14,None,None)),(35,(32,None,None),(40,None,None)))
for v in YieldBST(T):
	conn.sendall(str(v).encode('utf-8'))


s = MakeServerSocket()



conn.recv(6)
	
	

	
