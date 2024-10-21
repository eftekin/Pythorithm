# Exceptions in Python are errors that occur during execution, which disrupt the normal flow of a program.
# Instead of crashing the program, exceptions can be handled to prevent unwanted behaviors.

# Section 1: Built-in Exceptions
# Python provides several built-in exceptions like ValueError, TypeError, IndexError, and many more.
# Example:
try:
    print(10 / 0)  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Exception caught: {e}")


# Section 2: Raising Exceptions
# You can manually raise exceptions using the `raise` keyword.
# Example:
def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    return "You are allowed."


try:
    print(check_age(16))
except ValueError as e:
    print(f"Raised Exception: {e}")

# Section 3: Try / Except
# `try` and `except` blocks are used to handle exceptions.
# The code inside the `try` block is executed. If an exception occurs, it moves to the `except` block.
try:
    num = int(input("Enter a number: "))
    print(f"Your number is: {num}")
except ValueError:
    print("That's not a valid number!")

# Section 4: Catching Specific Exceptions
# You can catch specific exceptions to handle different types of errors in various ways.
try:
    print("Your result:", 10 / int(input("Enter a number: ")))
except ValueError:
    print("You must enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Section 5: Handling Multiple Exceptions
# You can catch multiple exceptions using multiple `except` blocks or a single block for multiple exceptions.
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except (FileNotFoundError, IOError) as e:
    print(f"Error occurred: {e}")

# Section 6: The else Clause
# The `else` clause is executed only if no exception is raised in the `try` block.
try:
    num = int(input("Enter a number: "))
    print(f"Your number is: {num}")
except ValueError:
    print("That's not a valid number!")
else:
    print("Successfully entered a valid number.")

# Section 7: The finally Clause
# The `finally` block is always executed, regardless of whether an exception occurred or not.
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution complete. Cleaning up...")


# Section 8: User-defined Exceptions
# You can define your own exceptions by subclassing the built-in Exception class.
class CustomError(Exception):
    pass


def raise_custom_error(condition):
    if condition:
        raise CustomError("A custom error occurred!")


try:
    raise_custom_error(True)
except CustomError as e:
    print(f"User-defined exception caught: {e}")


# Section 9: Customizing User-defined Exceptions
# You can customize user-defined exceptions by adding extra properties or methods.
class AgeError(Exception):
    def __init__(self, age, message="Age is invalid."):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} -> {self.message}"


try:
    raise AgeError(15, "You must be 18 or older.")
except AgeError as e:
    print(f"Custom Exception: {e}")
