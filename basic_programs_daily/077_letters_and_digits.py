# Write a program that accepts a sentence and calculate the number of letters and
# digits. Suppose the following input is supplied to the program:

# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print("LETTERS", letter_count)
print("DIGITS", digit_count)
