def find_duplicates(str):
    char_count = {}
    duplicates = []

    for i in str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)

    return duplicates


input_str = "mustafa eftekin"

duplicate_chars = find_duplicates(input_str)

print("Duplicate characters:", duplicate_chars)
