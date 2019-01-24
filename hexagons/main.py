position = [0, 0, 0]
distance = 0

def move(direction):
	if direction == "n":
		position[0] -= 1
		position[2] += 1
	elif direction == "nw":
		position[0] -= 1
		position[1] += 1
	elif direction == "ne":
		position[1] -= 1
		position[2] += 1

	elif direction == "s":
		position[0] += 1
		position[2] -= 1
	elif direction == "sw":
		position[1] += 1
		position[2] -= 1
	elif direction == "se":
		position[0] += 1
		position[1] -= 1
	else:
		print("Error: Invalid direction provided!\nThe direction is:`" + direction + "`")

def calc_distance():
	sum = abs(position[0]) + abs(position[1]) + abs(position[2])
	return int(sum) / 2

with open("hexagony") as file:
	content = file.readline()
directions = content.split("\n")
directions = directions[0].split(",")

for direction in directions:
	move(direction)
	distance = max(distance, calc_distance())

print(position)
print (distance)
