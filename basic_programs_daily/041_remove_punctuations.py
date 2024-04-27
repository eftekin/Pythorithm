# Write a Python Program to Remove Punctuation From a String.

# define punctuations
punctuations = """!()-[];:'"\,<>./?@#$%^&*_~"""

# to take input from the user

my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""

for char in my_str:
    if char not in punctuations:
        no_punct += char

# display the unpunctuated string
print("\nUnpunctuated String: ", no_punct)
