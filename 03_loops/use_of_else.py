'''Else is used with for loop and while loop as well
when all value ends in loop and loop complete then only else used'''

for i in range(5):
    print(i)
    
    
else:
    print("Sorry no i")
    
###
for i in range(5):
    print(i)
    if i == 4:
        break
    
else:
    print("Sorry no i")