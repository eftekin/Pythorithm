# Write a Python program to find words which are greater than given length k.


def find_words(words, k):
    # create an empty list to store words greater than k
    result = []

    # itarete through each word in the list
    for i in words:
        # check if the length of the i is greater than k
        if len(i) > k:
            # if yes, append it to the result list
            result.append(i)

    return result


word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = 5
long_words = find_words(word_list, k)

print(f"Words longer than {k} characters: {long_words}")
