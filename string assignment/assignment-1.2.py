#1-  Write a Python program to Count all letters, digits, and special
#  symbols from the given string
#  Input = “P@#yn26at^&i5ve”
#  Output: Chars = 8 Digits = 2 Symbol = 3

def count_chars_digits_symbols(string):
  """Counts letters, digits, and special symbols in a given string."""
  chars = 0
  digits = 0
  symbols = 0

  for char in string:
    if char.isalpha():
      chars += 1
    elif char.isdigit():
      digits += 1
    else:
      symbols += 1

  return chars, digits, symbols

string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(string)

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)


# -----------------------------------------------------------------------------------------

# 2-Write a Python program to remove duplicate characters of a given
#  string.
#  Input = “String and String Function”
#  Output: String and Function

def remove_duplicates(string):
  """Removes duplicate characters from a given string."""
  result = ""
  for char in string:
    if char not in result:
      result += char
  return result

string = "String and String Function"
result = remove_duplicates(string)
print(result)

# -------------------------------------------------------------------------------------------

# 3- Write a Python program to count Uppercase, Lowercase, special
#  character and numeric values in a given string
# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
#  Output:
#  UpperCase : 5
#  LowerCase : 18
#  NumberCase : 5
#  SpecialCase : 11

def count_characters(string):
  """Counts uppercase, lowercase, digits, and special characters in a string."""
  uppercase = 0
  lowercase = 0
  digits = 0
  special_chars = 0

  for char in string:
    if char.isupper():
      uppercase += 1
    elif char.islower():
      lowercase += 1
    elif char.isdigit():
      digits += 1
    else:
      special_chars += 1

  return uppercase, lowercase, digits, special_chars

string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase, lowercase, digits, special_chars = count_characters(string)

print("UpperCase :", uppercase)
print("LowerCase :", lowercase)
print("NumberCase :", digits)
print("SpecialCase :", special_chars)

# --------------------------------------------------------------------------------------

# 4- Write a Python Count vowels in a string
#  input= “Welcome to Python Assignment”
#  Output: Total vowels are: 8

def count_vowels(string):
  """Counts the number of vowels in a given string."""
  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count

string = "Welcome to Python Assignment"
total_vowels = count_vowels(string)
print("Total vowels are:", total_vowels)

# --------------------------------------------------------------------------------------