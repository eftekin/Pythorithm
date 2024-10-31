# Write a simple Halloween-themed Python program called 'Ghostly Message.'
import random


def spooky_text(message):
    spooky_message = ""
    for char in message:
        if random.choice([True, False]):
            spooky_message += char.upper()
        else:
            spooky_message += char.lower()
    return spooky_message


print("👻 Welcome, spirits of Halloween! 👻")
user_message = input("Enter a Halloween message: ")
print("\n🎃 Your Spooky Message 🎃")
print(spooky_text(user_message))
