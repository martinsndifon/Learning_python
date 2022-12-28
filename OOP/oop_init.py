class person:
	def __init__(self, name):
		self.name = name
	
	def say_hi(self):
		print('Hello, my name is', self.name)
	
p = person('Martins')
p.say_hi()