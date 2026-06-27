cup = input("Choose your cup size (small/medium/large): ").strip().lower()

prices = {
    "small": 10,
    "medium": 15,
    "large": 20
}

if cup in prices:
    print(f"Price is {prices[cup]} rupees")
else:
    print("Unknown cup size")
