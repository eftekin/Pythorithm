# Write a program that accepts a sequence of whitespace separated words as input
# and prints the words after removing all duplicate words and sorting them
# alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# take input from the user
input_sequence = input("Enter a sequence of whitespace-seperated words: ")

# split the input into words and convert it into a set to remove duplicates
words = set(input_sequence.split())

# sort the unique words alphanumerically
sorted_words = sorted(words)

# join the sorted words into a string with whitespace separation
result = " ".join(sorted_words)

# print the result
print("Result:", result)
