# Array Generating Functions in Python
from numpy import * 

val = full(10,5) #array of size 10 with all values as 5
for x in val:
    print(x, end=", ")
    
print("\n")
val = zeros((3,5)) #3x5 array with all values as 0  
for row in val:
    for x in row:
        print(int(x), end=" ")
    print()

print("\n")
val = ones((2,4)) #2x4 array with all values as 1
for row in val:
    for x in row:
        print(int(x), end=" ")
    print()
    
print("\n")
val = eye(4) #4x4 identity matrix
for row in val:
    for x in row:
        print(int(x), end=" ")
    print()
