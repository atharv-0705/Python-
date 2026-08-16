# Array Insertion in Python
from array import *

arr = array('i',[])

n = int(input("Enter number of elements to insert in array: "))
for i in range(n):
    x = int(input(" Enter the number: "))
    arr.append(x)
    # or use arr.insert(i, x) to insert at specific position
    # arr.extend([x1, x2, x3]) to add multiple elements at once
    
    print(f"Enter the element: {x} | Array : {' '.join(map(str, arr))}")

'''
- map(str, arr) converts each element of the list arr into a string.
- ' '.join(...) joins them together with spaces in between, so the array prints nicely as a space-separated string.

map() is a built-in function that applies another function to every item in an iterable (like a list, tuple, or string)
and returns a special object called a map object (which you can convert to a list, set, etc.).
SYNTAX: 
map(function, iterable)
- function → the function you want to apply
- iterable → the sequence of values you want to process

Example 1: Converting numbers to strings

arr = [1, 2, 3, 4]
result = map(str, arr)   # applies str() to each element
print(list(result))

OUTPUT:
['1', '2', '3', '4']

Example 2: Doubling numbers

def double(n):
    return n * 2

numbers = [1, 2, 3, 4]
result = map(double, numbers)
print(list(result))

OUTPUT:
[2, 4, 6, 8]
'''
