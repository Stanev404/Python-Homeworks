class Fibs(object):
	k=0
	def __init__(self):
		self.prev1=0
		self.prev2=1
		self.res = 0
	def next(self):
		if(Fibs.k==0):
			Fibs.k=Fibs.k+1
			return 0
		if(Fibs.k==1):
			self.res = self.prev1 + self.prev2
			Fibs.k=Fibs.k+1
			return self.res
		self.res = self.prev1 + self.prev2

		self.prev1 = self.prev2
		self.prev2 = self.res
		return self.res
	def __iter__(self):
		return self
