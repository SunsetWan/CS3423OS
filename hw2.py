# hw2.py 
# 
# comments
# your code here
if __name__ == '__main__':
	def YieldBST(T):
		if type(T) is not tuple:
			if T is not None:
				yield T
		else:
			yield from YieldBST(T[1])
			yield from YieldBST(T[0])
			yield from YieldBST(T[2])
			
			
	L = []
	T = (17,(12,(6,None,None),(14,None,None)),(35,(32,None,None),(40,None,None)))
	for v in YieldBST(T):
		L.append(v)
	print(L)