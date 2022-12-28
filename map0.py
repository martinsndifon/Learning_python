matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def square_matrix_simple(matrix=[]):
	new_matrix = []
	for i in matrix:
		sub_list = list(map(lambda x: x*x, i))
		new_matrix.append(sub_list)
	return new_matrix

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)