# Cache Return Values
''' Implement a decorator that caches the return values of a function,
so that when it's called with the same arguments,
the cached value is returned istead of re-excuting the function.'''

import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            print("Returning cached value")
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))  # Takes 4 seconds
print(long_running_function(2, 3))  # Returns cached value immediately
print(long_running_function(4, 5))  # Takes 4 seconds