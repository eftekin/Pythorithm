# Write a function that stutters a word as if someone is struggling to read it. The first
# two letters are repeated twice with an ellipsis ... and space after each, and then the
# word is pronounced with a question mark ?.
# Examples
# stutter("incredible") ➞ "in... in... incredible?"
# stutter("enthusiastic") ➞ "en... en... enthusiastic?"
# stutter("outstanding") ➞ "ou... ou... outstanding?"
# Hint :- Assume all input is in lower case and at least two characters long.


def stutter(word):
    if len(word) < 2:
        return "Word must be at least two characters long."

    stuttered_word = f"{word[:2]}... {word[:2]}... {word}?"
    return stuttered_word


# test cases
print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))
