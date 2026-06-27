#PRIME NUMBER CHECKER
'''Check the number is prime'''

number = 31

is_prime = True
if number > 1:
    for i in range(2, number):
        if (number % i)== 0:
            is_prime = False
            break
print(number, "is a Prime Number: ", is_prime)