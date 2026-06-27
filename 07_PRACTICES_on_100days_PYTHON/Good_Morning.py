"""Create a python program capable of greeting you with Good Morning.
Your program should use time module to get the current hour.
Here a sample program and documentation like for you."""
# Hour:Minute:Second
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("GOOD MORNING ATHARV!")
elif(hour>=12 and hour<17):
    print("GOOD AFTERNOON ATHARV!")
else: 
    print("GOOD EVENING ATHARV!")
    