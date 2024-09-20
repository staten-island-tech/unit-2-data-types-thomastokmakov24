""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """
""" import string
x=input () 
y=x.split()
string.count () """
""" import string

x = input("Enter a string: ")
y = x.split()

word_count = {word: y.count(word) for word in y}
print(word_count) """
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
elif day_of_week == "Saturday":
    print("")
else:
    print("incorrect")