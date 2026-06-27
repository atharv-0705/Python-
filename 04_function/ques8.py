# FUNCTION WITH *kwargs
'''Create a function that accepts any number of keyword arguments 
and prints them in he format'''

def print_kwargs (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    
print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer",
enemy="Dr. Jackaal")
