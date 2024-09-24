""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
elif day_of_week == "Saturday":
    print("day after")
else:
    print("incorrect") """
""" x = "test"
print(f"hello {x}") """
""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """
""" x = int(input())
if x % 2 ==0:
    print("even")
else:
    print("odd") """

def calculate_tip(bill, money):
money= float(int(input("How much was your check?")))
bill= input("How was your customer service?")
if bill== "bad":
    print("0% tip")
    return money
elif bill== "okay":
    print("15% tip")
    return money*1.15
elif bill== "good":
    print("20% tip")
    return money*1.2
elif bill== "great":
    print("25% tip")
    return money*1.25
else:
    print("response not understood. Try using the words bad,okay,good, or great.")

""" 
    tips = {'bad': 0, 'okay': 0.15, 'good': 0.20, 'great': 0.25}
return money *  bill
 """