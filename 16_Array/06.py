# Array Generating Functions in Python  
from array import array
from numpy import *

val = array([1,2,3,4,5.5,'A']) #Creating Heterogeneousarray using array module
for x in val:
    print(x, end=', ')
print("\n")

arr = array([1,2,3,4,5], float)
for x in arr:
    print(x, end=', ')
print("\n")

val = linspace(10,20,11) #11 numbers from 10 to 20
for x in val:
    print(x, end=", ")
    
print("\n")
val = arange(10,20,2) #numbers from 10 to 20 with step 2
for x in val:
    print(x, end=", ")
    
print("\n")
val = logspace(1,10,5) #5 numbers from 10^1 to 10^10
for x in val:
    print(x, end=", ")