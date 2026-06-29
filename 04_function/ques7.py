# FUNCTION WITH *args
'''Write a function that takes variable number of arguments and return their sum'''

def sum_all(*args): #*args is used to pass variable number of arguments
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)     
    return sum(args) #sum() function is used to calculate sum of all elements in an iterable

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
