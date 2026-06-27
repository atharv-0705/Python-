def func1():
    try:
        l = [1, 4, 5, 6]
        i = int(input("Enter the index: "))  # User inputs an index
        print(l[i])                          # Tries to print the element at that index
        return 1                             # Returns 1 if successful
    except:
        print("Some error occured")          # Catches any error (e.g., invalid index or input)
        return 0                             # Returns 0 if an error occurs
    finally:
        print("I am always executed")        # Always runs, regardless of success or failure

x = func1()
print(x)
