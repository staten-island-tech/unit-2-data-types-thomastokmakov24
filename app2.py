""" def calculate_tip():
    money = float(input("How much was your check?Please enter only numerical values and decimal points. "))
    customer = input("How was your customer service?Please do not use any capitals, spaces, or any other answers than the words bad, okay, good, or great. ")

    if customer == "bad":
        tip_percentage = 0
    elif customer == "okay":
        tip_percentage = 0.15
    elif customer == "good":
        tip_percentage = 0.20
    elif customer == "great":
        tip_percentage = 0.25
    else:
        print("Response not understood. Try using the words bad, okay, good, or great.")
        return None  

    tip_amount = money * tip_percentage
    total_amount = money + tip_amount

    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount (including tip): ${total_amount:.2f}")
    return total_amount

calculate_tip()
 """
""" def find_factors(n):
    if n <= 0:
        print("Please enter a positive whole number.")
        return []

    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

number = int(input("Enter a positive whole number. "))
factors = find_factors(number)
print(f"The factors of {number} are: {factors}")

 """
a=int(input("numero uno"))
b=int(input("numero dos"))
for i in range(2,a+1):
    if a%i==0 and b:
        return i{-1}