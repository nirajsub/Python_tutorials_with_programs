# 1. Arithmetic Operators:
# Addition (+): Adds two operands together.
result = 10 + 5  # result will be 15
print("Addition:", result)
# Subtraction (-): Subtracts the second operand from the first.
result = 10 - 5  # result will be 5
print("Subtraction:", result)
# Multiplication (*): Multiplies two operands.
result = 10 * 5  # result will be 50
print("Multiplication:", result)
# Division (/): Divides the first operand by the second, yielding a float.
result = 10 / 5  # result will be 2.0
print("Division:", result)
# Floor Division (//): Divides the first operand by the second, yielding an integer.
result = 10 // 3  # result will be 3
print("Floor Division:", result)
# Modulo (%): Returns the remainder of the division.
result = 10 % 3  # result will be 1
print("Modulo:", result)
# Exponentiation (**): Raises the first operand to the power of the second.
result = 2 ** 3  # result will be 8
print("Exponentiation:", result)

# 2. Assignment Operators:
# Assignment (=): Assigns a value to a variable.
x = 10
print("Assignment (=)", x)
# Compound Assignment (e.g., +=, -=, *=): Performs an arithmetic operation and assigns the result to the variable.
x += 5  # equivalent to x = x + 5
print("Compound Assignment (e.g., +=, -=, *=)", x)

# 3. Comparison Operators:
# Equal to (==): Checks if two operands are equal.
result = 5 == 5  # result will be True
print("Equal to:", result)
# Not equal to (!=): Checks if two operands are not equal.
result = 5 != 10  # result will be True
print("Not equal to:", result)
# Greater than (>), Less than (<), Greater than or equal to (>=), Less than or equal to (<=): Compare the magnitude of two operands.
result = 5 > 3  # result will be True
print("Greater than:", result)

# 4. Logical Operators:
# and: Returns True if both operands are True.
result = True and False  # result will be False
print("and:", result)
# or: Returns True if either of the operands is True.
result = True or False  # result will be True
print("or:", result)
# not: Negates the value of the operand.
result = not True  # result will be False
print("not:", result)

# 5. Membership Operators:
# in: Returns True if a value is found in a sequence.
result = 3 in [1, 2, 3]  # result will be True
print("in:", result)
# not in: Returns True if a value is not found in a sequence.
result = 4 not in [1, 2, 3]  # result will be True
print("not in:", result)

# 6. Identity Operators:
# is: Returns True if two operands refer to the same object.
result = "hello" is "hello"  # result will be True
print("is:", result)
# is not: Returns True if two operands do not refer to the same object.
result = "hello" is not "world"  # result will be True
print("is not:", result)
