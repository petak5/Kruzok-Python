# x and y direction
vec = (0, 1)	# UP - vector
pos = (0, 0)	# position


with open("vstup1.txt") as file:
	content = file.readlines()
commands = content[0].split(", ")

for command in(commands):
	if command[0] == "R":

		# BEWARE OF HEAVY LOGIC
		if vec[1] == 1:		# turn RIGHT
			vec = (1, 0)
		elif vec[0] == 1:	# turn DOWN
			vec = (0, -1)
		elif vec[1] == -1:	# turn LEFT
			vec = (-1, 0)
		elif vec[0] == -1:	# turn UP
			vec = (0, 1)
		else:
			print("Something went wrong in 'R' branch")
		# UR SAFE HERE

		size_of_move = int(command.split("R")[1])

		move = (size_of_move * vec[0], size_of_move * vec[1])
		pos = (pos[0] + move[0], pos[1] + move[1])

	elif command[0] == "L":
		# BEWARE OF HEAVY LOGIC
		if vec[1] == 1:		# turn LEFT
			vec = (-1, 0)
		elif vec[0] == -1:	# turn DOWN
			vec = (0, -1)
		elif vec[1] == -1:	# turn RIGHT
			vec = (1, 0)
		elif vec[0] == 1:	# turn UP
			vec = (0, 1)
		else:
			print("Something went wrong in 'L' branch")
		# UR SAFE HERE

		size_of_move = int(command.split("L")[1])

		move = (size_of_move * vec[0], size_of_move * vec[1])
		pos = (pos[0] + move[0], pos[1] + move[1])
	else:
		print("Error: Command not detected")
x = pos[0]
y = pos[1]
distance = abs(x) + abs(y)
print(distance)
