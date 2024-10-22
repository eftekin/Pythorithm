# Create a function that replaces all the vowels in a string with a specified character.
# Examples
# replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
# replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
# replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"


def replace_vowels(string, char):
    vowels = "AEIOUaeiou"  # List of vowels to be replaced
    for vowel in vowels:
        string = string.replace(vowel, char)  # replace each vowel
    return string


# test cases
print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
