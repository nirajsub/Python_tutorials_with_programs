# Declare any two variable
num1 = 5
num2 = 7
# Add two number with '+' operator
sum = num1 + num2
# This will print the result
print(f"The sum of {num1} and {num2} is: {sum}")

# Now let's take input from user
num1 = input("Enter first number: ") # Prompt the user to enter the first number
num2 = input("Enter first number: ") # Prompt the user to enter the second number
sum = num1 + num2 # This will concatenate the two values because it will take the value of num1 and num2 as strings, not perform addition
print(f"The sum of {num1} and {num2} is: {sum}")

# To perform addition, you need to convert the input values to integers or floats
actualsum = int(num1) + int(num2) # Convert num1 and num2 to integers and perform addition 
print(f"The actual sum of {num1} and {num2} is: {actualsum}") 
# This could generate an error as 'invalid literal for int()' if you input decimal value. So check it once and comment this out.


# You can convet the value as float so that you can add decimal integer also.
actualsum = float(num1) + float(num2) # Convert num1 and num2 to floats and perform addition
print(f"The actual sum of {num1} and {num2} is: {actualsum}")



