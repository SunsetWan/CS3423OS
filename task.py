class Task:
	def __init__(self, name, release, cpuBurst):
		self.name = name
		Rtime = 'rtime'
		cpuBurst = 'cpuBurst'
		
	def __repr__(self):
		return self.__class__.__name__ + '(%s, %d, %d)' % (repr(self.name),l)