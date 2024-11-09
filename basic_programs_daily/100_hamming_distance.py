# Hamming distance is the number of characters that differ between two strings.
# To illustrate:
# String1: "abcbba"
# String2: "abcbda"
# Hamming Distance: 1 - "b" vs. "d" is the only difference.
# Create a function that computes the hamming distance between two strings.
# Examples
# hamming_distance("abcde", "bcdef") ➞ 5
# hamming_distance("abcde", "abcde") ➞ 0
# hamming_distance("strong", "strung") ➞ 1


def hamming_distance(str1, str2):
    # Check if the strings have the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")
    # Initialize a counter to keep track of differences
    distance = 0
    # Iterate through the characters of both strings
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1  # Increment the counter for differences
    return distance


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
