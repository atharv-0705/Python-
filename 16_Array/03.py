# Array Slicing in Python
from array import *

val = array('i',[1, 2, 3, 4, 5, 6, 7, 8, 9])

abc = val[2:5]
for i in range(0,len(abc)):
    print(abc[i],end=", ")
    
print("\n")
abc = val[2:-3]
for i in range(0,len(abc)):
    print(abc[i],end=", ")
    
print("\n")
abc = val[::-1]
for i in range(0,len(abc)):
    print(abc[i],end=", ")
    
    