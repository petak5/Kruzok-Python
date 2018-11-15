field = [[0,  0,   1,   0,  0],		# keypad
	[0,  2,   3,   4,  0],
	[5,  6,   7,   8,  9],
	[0, 'A', 'B', 'C', 0],
	[0,  0,  'D',  0,  0]]

position = (2, 0)	# 0 is Y and 1 is X

def clampY(pos):
	# increments the X coordinates (1) but clamps the Y axis
	if (pos[1] == 0):
		pos = (2, 0)
	elif pos[1] == 1:
		if pos[0] < 1:
			pos = (1, 1)
		elif pos[0] > 3:
			pos = (3, 1)
	elif pos[1] == 2:
		if pos[0] < 0:
			pos = (0, 2)
		elif pos[0] > 4:
			pos = (4, 2)
	elif pos[1] == 3:
		if pos[0] < 1:
			pos = (1, 3)
		elif pos[0] > 3:
			pos = (3, 3)
	elif (pos[1] == 4):
		pos = (2, 4)

	return pos

def clampX(pos):
	# increments the Y coordinates (0) but clamps the X axis
	if pos[0] == 0:
		pos = (0, 2)
	elif pos[0] == 1:
		if pos[1] < 1:
			pos = (1, 1)
		elif pos[1] > 3:
			pos = (1, 3)
	elif pos[0] == 2:
		if pos[1] < 0:
			pos = (2, 0)
		elif pos[1] > 4:
			pos = (2, 4)
	elif pos[0] == 3:
		if pos[1] < 1:
			pos = (3, 1)
		elif pos[1] > 3:
			pos = (3, 3)
	elif pos[0] == 4:
		pos = (4, 2)
	
	return pos

with open("vstup2.txt") as file:
	content = file.readlines()
for instructions in content:
	for instruction in instructions:
		"""if instruction != "\n":
			print("Actual position: " + str(position) + " INS: " + instruction + " CHAR: " + str(field[position[0]][position[1]]))"""
		if instruction == 'U':
			position = (position[0] - 1, position[1])
			position = clampY(position)
		elif instruction == 'D':
			position = (position[0] + 1, position[1])
			position = clampY(position)
		elif instruction == 'L':
			position = (position[0], position[1] - 1)
			position = clampX(position)
		elif instruction == 'R':
			position = (position[0], position[1] + 1)
			position = clampX(position)
	print(field[position[0]][position[1]])
