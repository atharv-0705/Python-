# VALIDATE input
'''Keep asking the user for input until they enter a number
b/w 1 and 100'''

while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("THANKS")
        break
    else:
        print("TRY AGAIN")
