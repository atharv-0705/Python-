# AGE GROUP CATEGORIZATION

'''Classify a person's age group:
child(<13), teenage(13-19), adult(20-59), senior(60+)'''

age = int(input())

if age < 13:
        print("Child")
elif age < 20:
        print("Teenager")
elif age < 60:
        print("Adult")
else:
        print("Senior")