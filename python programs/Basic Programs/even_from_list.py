input_list = [1, 2, 3, 4, 5, 6]
# output = []
# for num in input_list:
#     if num % 2 == 0:
#         output.append(num)
output = [num for num in input_list if num % 2 == 0]


print(output)

def check_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

print(check_prime(10))