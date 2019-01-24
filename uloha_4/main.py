expressions = []
registers = {}

def condition_passed(register, operator, value):
	if register not in registers:
		registers[register] = 0

	if operator == "==":
		return (registers[register] == value)
	elif operator == "!=":
		return (registers[register] != value)
	elif operator == ">":
		return (registers[register] > value)
	elif operator == ">=":
		return (registers[register] >= value)
	elif operator == "<":
		return (registers[register] < value)
	elif operator == "<=":
		return (registers[register] <= value)
	else:
		print("Error: No valid operator provided! Operator is: `" + operator + "`")
		return False

with open("vstup") as file:
	instructions = file.readlines()

for instruction in instructions:
	temp = instruction.split("\n")
	del temp[1]
	expressions += temp

for expression in expressions:
	expression = expression.split(" ")

	if expression[0] not in registers:
		registers[expression[0]] = 0
	if condition_passed(expression[4], expression[5], int(expression[6])):
		if expression[1] == "inc":
			registers[expression[0]] += int(expression[2])
		elif expression[1] == "dec":
			registers[expression[0]] -= int(expression[2])
		else:
			print("Error: Condition passed, but neither `inc` or `dec` matched!")

max = 0
for i in registers:
	if registers[i] > max:
		max = registers[i]

print(max)
