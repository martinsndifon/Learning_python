name = "martins.ndifon? mgbe:evareh emmanuel. michael?ifere."

i = 0
while i < len(name):
	if name[i] == '.' or name[i] == '?' or name[i] == ':':
		print(f'{name[i]}', end='')
		print('\n')
		i += 1
		if i < len(name):
			if name[i] == ' ':
				i += 1
			else:
				continue
	else:
		print(f'{name[i]}', end='')
		i += 1