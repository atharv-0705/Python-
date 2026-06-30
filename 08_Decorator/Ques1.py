# Timing Function Execution
''' Write a decorator that measures the time
a function takes to excute'''

import time

def timer(func): #Decorator function to measure time
    def wrapper(*args, **kwargs): #Wrapper function to measure time
        start = time.time()        #Start time before function execution
        result = func(*args, **kwargs)  #Function execution
        end = time.time()   #End time after function execution
        print(f"Function {func.__name__} took {end - start} seconds to execute.")   
        return result  #Return the result of the function
    return wrapper   #Return the wrapper function

@timer                  #Decorator applied to the function for timing
def example_function(n):  #Example function to demonstrate the timer decorator
    time.sleep(n)         #Simulate a function that takes n seconds to execute
        
        
example_function(2)  