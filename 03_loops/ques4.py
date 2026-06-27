#REVERSE A STRING
'''Reverse a string using a loop'''

input_str = "PYTHON"
reversed_str = ""

for char in input_str:
    reversed_str =char + reversed_str
print(reversed_str)