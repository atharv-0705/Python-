# Array Copying and Modifying in Python
from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

copyArr = array(val.typecode ,(x*2 for x in val))

print("Array elements after copying and modifying:")
for i in range(0,len(val)):
    print("Original array element:", val[i], "  Copied array element:", copyArr[i])

print("\n")

copyArr.remove(18)
copyArr.pop(0)
print("Array elements after removing elements from copied array:")
for i in range(0,len(copyArr)):
    print(copyArr[i],end=", ")    