my_list = list(range(1, 11))
print(my_list)

def timestwo(num):
	return num * 2

print(list(map(timestwo, my_list)))

import random

randlist = list(random.randint(1, 1001) for i in range(100))

print(list(filter((lambda x: x % 9 == 0), randlist)))