num = 25
sqrt = num ** 0.5
print(sqrt)

# Taking input from user
num = float(input("Enter the number to find the square root of: "))
sqrt = num ** 0.5
print(f"The square root of {num} is {sqrt}")

import cmath
num = 25
sqrt = cmath.sqrt(num)
print(sqrt)

num = eval(input("Enter the number to find the square root of: "))
sqrt = cmath.sqrt(num)
print(sqrt)