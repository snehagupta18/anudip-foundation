#1- Declare a div() function with two parameters. Then call the function and pass two
# numbers and display their division.

def div(a, b):
  """Divides two numbers and returns the result."""
  if b == 0:
    return "Division by zero is not allowed"
  else:
    return a / b

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the div function and print the result
result = div(num1, num2)
print("The division of", num1, "and", num2, "is:", result)

# ------------------------------------------------------------------------------------------------

#2- Declare a square() function with one parameter.Then call the function and pass
# one number and display the square of that number

def square(num):
  """Calculates the square of a number."""
  return num * num

# Get input from the user
number = float(input("Enter a number: "))

# Call the square function and print the result
result = square(number)
print("The square of", number, "is:", result)

# --------------------------------------------------------------------------------------------


#3- Using max() and min() functions display the maximum and minimum of 5 random
# numbers

import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for _ in range(5)]

# Find the maximum and minimum values
maximum = max(numbers)
minimum = min(numbers)

print("Random numbers:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)

# -----------------------------------------------------------------------------------------------

#4- Accept a name from the user and display that in lower case using lower()
#  function

name = input("Enter your name: ")
lower_case_name = name.lower()
print("Lowercase name:", lower_case_name)
# ---------------------------------------------------------------------------------------------