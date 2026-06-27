# 13/08

s = "MirSir"
print(s)
print (s[0])
print (s[2])
print (s[-1])
print (len(s))
print(s[0:3])
print(s[0:])
print (s[:])


a = "programming"
print(a[:])
print(len(a))
print(a[-5])
print (a[0:6:2])

print (a.count("m"))
print (a.count("mm"))

print(a.endswith("ing"))

print(a.capitalize())

print(a.find('i'))
print(a.find('in'))

print(a.replace('ing','er'))
course = 'Python C++ DSA Probablity Computer Networks'
print (course)
print (course.split(' '))

vowels = "aeiou"
count = sum(1 for char in a if char in vowels)
print("Number of vowels:", count)



#take string for user and split no. of words and identify wheather RAM is in the string or not
Names = 'Chetan ,ATHARV ,VAIBHAVI ,RAM '
print(Names.split(','))
if 'RAM' in Names:
    print('RAM is in the string : True')
else:
    print('RAM is in the string : False')