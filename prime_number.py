num = int(input("Enter a number: "))
if num == 1:
    print(num, "is neither prime nor composite")
elif num > 1:
    is_prime = True
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is a composite number")

# Here is another way to do it in more optimize way
import math

num = int(input("Enter a number: "))

if num < 2:
    print(num, "is neither prime nor composite")  # Numbers less than 2 are neither prime nor composite
elif num == 2:
    print(num, "is a prime number")  # 2 is a prime number
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):  # Iterate up to the square root of the number since factors of num will not be greater than its square root. This reduces the number of iterations required.
        if num % i == 0:  # If a factor is found
            is_prime = False  # Number is not prime
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is a composite number")


