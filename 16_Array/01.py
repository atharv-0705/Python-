# Array Operations in Python
from array import * 

val = array('i',[1, 2, 3, 4, 5, 6, 7, 8, 9]) #Creating array with integer type

print("Array in elements:")
for i in range(0,6):
#for i in range(0,len(val)): 
    print(val[i], end=": ")
    
    for x in val:
        print(x, end=",")
    print("\n") 
    
print(val.typecode)  #Printing type code of array

val.reverse()  #Reversing the array
print("Array elements after reversing:")
for i in range(0,len(val)):
    print(val[i], end=", ")
    
val.insert(3,10)  #Inserting value 10 at index 3
val.append(100) #Appending value 100 at the end of array
val[2] = 50  #Updating value at index 2 to 50
print("\nArray elements after inserting 10 at index 3 and appending 100 and updating index 2 to 50:")
for i in range(0,len(val)):
    print(val[i], end=", ")
 
