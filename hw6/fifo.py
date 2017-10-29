class FIFO:
	def __init__(self, initList=[]):
		self.A = list(initList)
		
	def get(self): # remove element and return itse value
		return self.A.pop(0) # throws underflow exception if empty
		
	def put(self, val): # add element
		self.A.append(val)
		
	def head(self): # A[0] if not empty, None instead of underflow exception
		return len(self.A) and self.A[0] or None
		
	def __iter__(self): # iterator over its elements
		for i in self.A: # convertable to tuple, list, for-in loop, etc
			yield i
			
	def __len__(self): # allows caller to call len(f) where f is FIFO
		return len(self.A)
		
	def __repr__(self): # shows a representation; we just show it as list
		return repr(self.A)
		
