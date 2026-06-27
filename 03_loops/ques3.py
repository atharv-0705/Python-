# MULTIPLICATION TABLE PRINTER
'''Print the multiplication table foe a given up to 10,
but skip the 5th iteration'''

number = 3

for i in range(1,11):
    if i == 5:
        continue
    print(number,"X",i,"=", number * i)