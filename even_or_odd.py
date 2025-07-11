# even_or_odd.py

# Task 1: Check if a Number is Even or Odd

try:
    num = int(input("Enter an integer: "))

    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
