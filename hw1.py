# hw1.py 
# Name: Wan Chenxi, Student ID: x1067086 
# comments
# your code here
def PrintBST(T):
	if type(T) is not tuple:
		if T is not None:
		  print(T)
	else:
		PrintBST(T[1])
		PrintBST(T[0])
		PrintBST(T[2])

# begin built-in test case follows your code in the same .py file # the test case is run when you run this file as top-level, # but not if it is imported into another Python program as a module 
 #if __name__ == '__main__':
T = (17,(12,(6,None,None),(14,None,None)),(35,(32,None,None),(40,None,None)))
PrintBST(T)
