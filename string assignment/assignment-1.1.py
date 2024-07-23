# 1- Write a Python program to count the occurrences of each word in a
#  given sentence
#  string = “To change the overall look of your document. To change the look
#  available in the gallery”

def count_word_occurrences(sentence):
  """Counts the occurrences of each word in a given sentence."""
  words = sentence.split()
  word_count = {}

  for word in words:
    word_count[word] = word_count.get(word, 0) + 1

  return word_count

string = "To change the overall look of your document. To change the look available in the gallery"
word_counts = count_word_occurrences(string)

for word, count in word_counts.items():
  print(f"{word}: {count}")

# ----------------------------------------------------------------------------------------------

#2- Write a Python program to remove a newline in Python
#  String = "\nBest \nDeeptech \nPython \nTraining\n"

string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove leading and trailing newlines
string = string.strip()

# Remove internal newlines
string = string.replace("\n", " ")

print(string)


# ------------------------------------------------------------------------------------------

# 3- Write a Python program to reverse words in a string
#  String = “Deeptech Python Training”

def reverse_words(string):
  """Reverses the order of words in a string."""
  words = string.split()
  reversed_words = words[::-1]
  return " ".join(reversed_words)

string = "Deeptech Python Training"
reversed_string = reverse_words(string)
print(reversed_string)

# ---------------------------------------------------------------------------------------------

#4- Write a Python program to count and display the vowels of a given
#  text
#  String=”Welcome to python Training”

def count_vowels(text):
  """Counts the occurrences of vowels in a given text."""
  vowels = "aeiouAEIOU"
  vowel_count = 0

  for char in text:
    if char in vowels:
      vowel_count += 1

  return vowel_count

string = "Welcome to python Training"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)


# --------------------------------------------------------------------------------------------------------