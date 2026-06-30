# Debugging Function Calls
''' Create a decorator to print the function name and
the values of its arguments each time the function is called '''

def debug(func):   #Decorator function to debug function calls
    def wrapper(*args, **kwargs):                        #Wrapper function to debug function calls
        args_value = ', '.join(str(arg) for arg in args) #Get positional arguments as string
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items()) #Get keyword arguments as string
        
        print(f"Calling: {func.__name__} with arg {args_value} and kwargs {kwargs_value}")  #Print function name and arguments
        
        result = func(*args, **kwargs)                    #Function execution
        print(f"{func.__name__} returned {result}")       #Print the return value
        return result                                     #Return the result of the function
    return wrapper                                        #Return the wrapper function


@debug
def hello():
    print("Hello !")

@debug
def greet(name, greeting = "Hello"):
    print( f"{greeting}, {name}!")
    
hello()
greet("BAWA ", greeting= "✌️")


