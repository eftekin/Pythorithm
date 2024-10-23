# Python Testing Lesson
import unittest
import warnings

from parameterized import parameterized  # Requires the `parameterized` module


# Section 1: The assert Statement
# The `assert` statement is used to check if a condition is true.
# If the condition is false, an AssertionError is raised with an optional error message.
def test_positive_number(number):
    assert number > 0, "Number must be positive."


try:
    test_positive_number(-5)
except AssertionError as e:
    print(f"AssertionError: {e}")

# Section 2: Unit Testing
# Unit tests are small tests that verify the behavior of individual units of code, such as functions or methods.
# Each test is designed to check for specific behavior, and multiple tests are grouped in a test case.

# Section 3: Python's unittest Framework
# The `unittest` framework is Python's standard library for writing and running tests.


# Example test case using unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")  # Checks if 'foo' is converted to 'FOO'

    def test_isupper(self):
        self.assertTrue("FOO".isupper())  # Checks if the string is all uppercase
        self.assertFalse("Foo".isupper())  # Checks if 'Foo' is NOT all uppercase


# Section 4: Assert Methods I - Equality and Membership
# The `unittest` framework provides several assert methods, such as `assertEqual`, `assertIn`, `assertNotIn`.
class TestEquality(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(10, 10)  # Passes if both values are equal
        self.assertNotEqual(10, 5)  # Passes if values are not equal

    def test_membership(self):
        self.assertIn(3, [1, 2, 3])  # Passes if 3 is in the list
        self.assertNotIn(4, [1, 2, 3])  # Passes if 4 is not in the list


# Section 5: Assert Methods II - Quantitative Methods
# Methods to assert comparisons: `assertGreater`, `assertLess`, `assertGreaterEqual`, `assertLessEqual`.
class TestQuantitative(unittest.TestCase):
    def test_quantitative(self):
        self.assertGreater(10, 5)  # Passes if 10 > 5
        self.assertLess(5, 10)  # Passes if 5 < 10
        self.assertGreaterEqual(10, 10)  # Passes if 10 >= 10
        self.assertLessEqual(5, 5)  # Passes if 5 <= 5


# Section 6: Assert Methods III - Exception and Warning Methods
# These methods allow you to test if specific exceptions or warnings are raised.


# assertRaises - used to check if an exception is raised
class TestExceptions(unittest.TestCase):
    def test_raise_exception(self):
        with self.assertRaises(
            ZeroDivisionError
        ):  # This test passes if ZeroDivisionError is raised
            1 / 0

    # Testing custom exceptions
    def test_custom_exception(self):
        class MyCustomError(Exception):
            pass

        def function_that_raises():
            raise MyCustomError("This is a custom error.")

        with self.assertRaises(MyCustomError):  # Test if MyCustomError is raised
            function_that_raises()


# assertWarns - used to test if a specific warning is raised


class TestWarnings(unittest.TestCase):
    def test_warning(self):
        def issue_warning():
            warnings.warn("This is a warning!", UserWarning)

        with self.assertWarns(UserWarning):  # Test passes if UserWarning is raised
            issue_warning()


# Section 7: Parameterizing Tests
# Parameterized tests allow you to run the same test logic with different sets of data.


class TestParameterized(unittest.TestCase):
    @parameterized.expand(
        [
            (5, 25),  # input: 5, expected: 25
            (6, 36),  # input: 6, expected: 36
            (7, 49),  # input: 7, expected: 49
        ]
    )
    def test_square(self, input, expected):
        self.assertEqual(
            input * input, expected
        )  # Test if square of input equals expected value


# Section 8: Test Fixtures
# Fixtures are used to set up the environment before each test (using `setUp`) and clean it up after the test (using `tearDown`).


class TestFixtureExample(unittest.TestCase):
    def setUp(self):
        print("Setting up the test environment...")
        self.test_list = [1, 2, 3]  # Initial setup for each test

    def tearDown(self):
        print("Tearing down the test environment...")
        self.test_list.clear()  # Clean up after each test

    def test_append(self):
        self.test_list.append(4)
        self.assertIn(
            4, self.test_list
        )  # Test if 4 is successfully appended to the list


# Section 9: Skipping Tests
# You can skip tests that are not applicable or ready using `@unittest.skip`, `skipIf`, and `skipUnless`.


class TestSkipping(unittest.TestCase):
    @unittest.skip("This test is skipped unconditionally.")
    def test_skipped(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(True, "Skipped because the condition is true")
    def test_skipped_conditionally(self):
        self.assertEqual(1, 1)

    @unittest.skipUnless(False, "Skipped because the condition is false")
    def test_skipped_unless(self):
        self.assertEqual(1, 1)


# Section 10: Expected Failures
# Sometimes, you expect certain tests to fail. In such cases, use `@unittest.expectedFailure`.


class TestExpectedFailures(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 2)  # This test will fail, but it's marked as expected.


unittest.main()
