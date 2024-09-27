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
"""def find_factors(n,z):
    if n <= 0 or z <= 0:
        print("Please enter only positive whole numbers.")
        return None
n=int(input("numero uno"))
z=int(input("numero dos"))
for i in range(2,n+1) and (2,z+1):
    if n%i==0 and z:
        return i{-1}


    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors

number = int(input("Enter a positive whole number. "))
factors = find_factors(number)
print(f"The factors of {number} and {number} are: {factors}")"""
def find_factors(n, z):
    if n <= 0 or z <= 0:
        print("Please enter only positive whole numbers.")
        return None

    factors_n = []
    factors_z = []

    # Find factors of n
    for i in range(1, n + 1):
        if n % i == 0:
            factors_n.append(i)

    # Find factors of z
    for i in range(1, z + 1):
        if z % i == 0:
            factors_z.append(i)

    # Find common factors
    common_factors = set(factors_n) & set(factors_z)

    return sorted(common_factors)

# Get user input
n = int(input("Enter the first positive whole number: "))
z = int(input("Enter the second positive whole number: "))

# Find and display common factors
factors = find_factors(n, z)
if factors is not None:
    print(f"The common factors of {n} and {z} are: {factors}")
