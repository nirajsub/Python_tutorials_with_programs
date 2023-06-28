# Examples of Python Keywords
# False
# True
# None
# and
# or
# not
# if
# else
# elif
# while
# for
# in
# break
# continue
# def
# return
# class
# try
# except
# finally
# import
# from
# as
# with
# raise
# assert
# lambda

# False, True, and None:
# False and True are Boolean values representing the logical values of false and true, respectively.
# # None represents the absence of a value and is often used to indicate the absence of a return value in functions.

is_active = False
is_valid = True
result = None

# and, or, and not:
# and, or, and not are logical operators used for combining and negating conditions.
a = True
b = False

if a and b:
    print("Both a and b are true")

if a or b:
    print("Either a or b is true")

if not b:
    print("b is false")

# if, else, and elif:
# if, else, and elif are used for conditional statements and control the flow of the program based on specific conditions.
num = 10

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

# while and for:
# while and for are used for loop statements to iterate over a sequence of values until a certain condition is met.
count = 0
while count < 5:
    print("Count:", count)
    count += 1

numbers = [1, 2, 3]
for num in numbers:
    print("Using for", num)

# break and continue:
# break is used to exit a loop prematurely, while continue is used to skip the remaining code in the current iteration and move to the next one.
for num in range(5):
    if num == 3:
        break
    print("Using break", num)

for num in range(5):
    if num == 3:
        continue
    print("Using continue", num)

# def and return:
# def is used to define user-defined functions.
# return is used to specify the value that a function should return.
def add_numbers(a, b):
    return a + b

result = add_numbers(2, 3)
print(result)

# class:
# class is used to define a class, which is a blueprint for creating objects.
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print("Area is: ", circle.area())

# try, except, and finally:
# try, except, and finally are used for exception handling to catch and handle potential errors in code execution.
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution complete")

# import and from:
# import and from are used to include modules or specific functions from modules into the current program.
import math
print(math.sqrt(25))

from datetime import datetime
current_time = datetime.now()
print(current_time)

# as:
# as is used for aliasing, allowing you to give an alternate name to a module or object.
import numpy as np
array = np.array([1, 2, 3])
total = np.sum(array)
print(total)

# with:
# with is used in the context manager construct to ensure proper acquisition and release of resources.
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# assert:
# assert is used for debugging purposes to check if a condition is true. If it's false, an AssertionError is raised.
num = 10

assert num > 0, "Number should be positive"
print("Assertion passed")

# lambda:
# lambda is used to define anonymous functions, also known as lambda functions.
multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)

# raise:
# raise is used to raise an exception explicitly.
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")


