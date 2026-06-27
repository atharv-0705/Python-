# SUM OF EVEN NUMBERS
'''Calcalate the sum of even numbers up to a given number n.'''

n = 10
sum_even = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum_even += 1
print("Sum of Even Number: ",sum_even)