# Assuming that we have some email addresses in the
# "username@companyname.com (mailto:username@companyname.com)" format,
# please write program to print the user name of a given email address. Both user
# names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com (mailto:john@google.com)
# Then, the output of the program should be:
# john


def extract_username(email):
    # Split the email address at  "@" to seperate the username and domain
    parts = email.split("@")

    # check if the email address has the expected format
    if len(parts) == 2:
        return parts[0]  # The username is the first part
    else:
        return "Invalid email format"


try:
    email = input("Enter an email address: ")
    username = extract_username(email)
    print(username)
except ValueError:
    print("Invalid input. Please enter a valid email address.")
