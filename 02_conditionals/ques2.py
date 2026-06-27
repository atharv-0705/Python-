# MOVIE TICKET PRICING
'''Movie tickets are priced based on age :
$12 for adult(18+), $8 for children
Everyone gets $2 discount on Wednesday'''

age = 22
day = "Wednesday"

price = 12 if age >=18 else 8

if day == "Wednesday":
    price = price - 2
    price -= 2
    
print("Ticket price for you is $",price)