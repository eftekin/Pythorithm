import re


def check_special_chat(in_str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'

    if re.search(pattern, in_str):
        return True
    else:
        return False


input_str = str(input("Enter a string: "))

contains_special = check_special_chat(input_str)

if contains_special:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
