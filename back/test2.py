class Thing:
	def doThing(self, x):
		if(self.value):
			print(x)
	def __init__(self, value):
		self.value = value
