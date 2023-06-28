num = 25
sqrt = num ** 0.5
print(sqrt)

# Taking input from user
num = float(input("Enter the number to find the square root of: "))
sqrt = num ** 0.5
print(f"The square root of {num} is {sqrt}")

# the another advance way of doing it is:
import cmath
num = eval(input("Enter the number to find the square root of: "))
sqrt = cmath.sqrt(num)
print(sqrt)
