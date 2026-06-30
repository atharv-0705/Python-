# Simple Example of Decordator
'''A Decorator in Python is a special function 
that allows you to modify or extend the behavior of another function
or method without changing its actual code.'''

def decorator(func):    #Decorator function 
    def wrapper():      #Wrapper function to add extra behavior
        print("Before calling the function.") #Extra behavior before function call
        func()  #Function execution
        print("After calling the function.") #Extra behavior after function call
    return wrapper #Return the wrapper function

@decorator   #Decorator applied to the function
def greet(): #Function to be decorated
    print("Hello, World!")
 
greet()

'''
- "decorator" is the decorator function.
- "wrapper" adds extra behavior before and after greet().
- "@decorator" applies the decorator to greet.
'''