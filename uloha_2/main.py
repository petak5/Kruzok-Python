field = [		# keypad
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
position = (1, 1)	# 2, 2 in fact, 0 indexed...

def clamp(pos):		# clamps a tuple in between 0 and 2
	if pos[0] > 2:
		pos = (2, pos[1])
	elif pos[0] < 0:
		pos = (0, pos[1])
	elif pos[1] > 2:
		pos = (pos[0], 2)
	elif pos[1] < 0:
		pos = (pos[0], 0)
	return pos

with open("vstup2.txt") as file:
	content = file.readlines()
for instructions in content:
	for instruction in instructions:
		if instruction == 'U':
			position = (position[0] - 1, position[1])
			position = clamp(position)
		elif instruction == 'D':
			position = (position[0] + 1, position[1])
			position = clamp(position)
		elif instruction == 'L':
			position = (position[0], position[1] - 1)
			position = clamp(position)
		elif instruction == 'R':
			position = (position[0], position[1] + 1)
			position = clamp(position)
	print(field[position[0]][position[1]])
