def MakeParkingLot(N):
	global sem # semaphore for the parking lot 
	global spots # list for the spots 
	global spotsSync # for synchronizing access to spots 
	spots = [None for i in range(N)] # your code to initialize sem and spotsSync
	# I think i will choose BoundedSemaphore, but i still have difficulty implementing it.