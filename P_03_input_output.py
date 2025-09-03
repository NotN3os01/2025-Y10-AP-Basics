# ask the user for their name
username = input("What is your name? ")

# ask the user for their favorite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve and square the user's favorite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num ** 2

# Greet the user

print(f"\nhi {username}, your favourite number is {fav_num}")

# Output the results of doubling, halving and
# squaring their favourite integer
print(f"double {fav_num} is {double}")
print(f"half {fav_num} is {halve}")
print(f"{fav_num} is {square}")
print()
print("Have a nice day")