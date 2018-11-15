count = 0

def is_triangle(a, b, c):
	return sum_of_smallest_double(a, b ,c) > max(a, b, c)

def sum_of_smallest_double(a, b, c):
	return a + b + c - max(a, b, c)

with open("vstup3") as file:
	content = file.readlines()

for triangle in content:
	triangle = triangle.split()		# Get rid of the spaces
	if is_triangle(int(triangle[0]), int(triangle[1]), int(triangle[2])):
		count += 1

print(count)
