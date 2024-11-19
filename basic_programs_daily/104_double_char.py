# Create a function that takes a string and returns a string in which each character is
# repeated once.
# Examples
# double_char("String") ➞ "SSttrriinngg"
# double_char("Hello World!") ➞ "HHeelllloo WWoorrlldd!!"
# double char("1234! ") ➞ "11223344!! "


def double_char(input_str):
    doubled_str = ""

    for char in input_str:
        doubled_str += char * 2

    return doubled_str


print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_ "))
