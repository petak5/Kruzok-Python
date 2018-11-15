count = 0
counter = 0
triangles = [[], [], []]

def is_triangle(a, b, c):
	return sum_of_smallest_double(a, b ,c) > max(a, b, c)

def sum_of_smallest_double(a, b, c):
	return a + b + c - max(a, b, c)

with open("vstup3") as file:
	content = file.readlines()

for triangle in content:
	triangle = triangle.split()		# Get rid of the spaces

	triangles[counter] = triangle

	counter	+= 1
	if counter == 3:
		counter = 0
		for i in range(3):
			if is_triangle(int(triangles[0][i]), int(triangles[1][i]), int(triangles[2][i])):
				count += 1

print(count)
