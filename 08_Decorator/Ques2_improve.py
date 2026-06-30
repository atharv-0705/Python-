
#  Improved Debug Decorator

import time
from datetime import datetime

def debug(func):
    def wrapper(*args, **kwargs):
        # Prepare arguments as strings
        args_value = ', '.join(str(arg) for arg in args) if args else "no positional args"
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else "no keyword args"
        
        # Timestamp before execution
        start_time = time.time()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Calling: {func.__name__} "
              f"with {args_value} and {kwargs_value}")
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        # Timestamp after execution
        end_time = time.time()
        elapsed = end_time - start_time
        
        # Print result info
        if result is not None:
            print(f"{func.__name__} returned {result} (execution time: {elapsed:.4f}s)")
        else:
            print(f"{func.__name__} finished execution (execution time: {elapsed:.4f}s)")
        
        return result
    return wrapper

# Example usage
@debug
def hello():
    print("Hello !")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

hello()
greet("BAWA", greeting="✌️")

'''🔎 What Changed
- Added default messages when no arguments are passed (no positional args, no keyword args).
- Skipped printing None when the function doesn’t return anything. Instead, it says finished execution.
- Cleaner, more readable debug logs.
'''


'''🔑 Features of This Improved Version
- ✅ Shows timestamp when the function is called.
- ✅ Logs arguments clearly (handles empty args/kwargs gracefully).
- ✅ Prints return value only if not None.
- ✅ Displays execution time for performance insight.
- ✅ Works with any function signature thanks to *args and **kwargs.
'''