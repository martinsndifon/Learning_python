class DogNameError(Exception):

	def __init__(self, *args, **kwargs):
		Exception.__init__(self, *args, **kwargs)
"""
the for loop below can be replace with a single line style using the
'any' keyword: if any(char.isdigit() for char in dogname):
					raise DognameError
"""
try:
	dogname = input("what is your dog's name: ")
	for char in dogname:
		if char.isdigit():
			raise DogNameError
except DogNameError:
	print("Your dog's name can't contain a number")