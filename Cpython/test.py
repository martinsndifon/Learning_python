import ctypes

# we load the dll
lib = ctypes.CDLL("./mylib.so")

# we call the function 
lib.hello()
