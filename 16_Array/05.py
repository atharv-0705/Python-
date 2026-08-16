# Array Sorting and Searching in Python
from array import *
    
arr = array('i' ,[12,13,14,11,29,344,53,97,69,380])
sorted_arr = array('i', sorted(arr))  #Sorting array using sorted() function
print("\nArray elements after sorting:")
print(sorted_arr)

i = arr.index(53)  #Getting index of element 53
print(f"Index of element 53 is: {i}")