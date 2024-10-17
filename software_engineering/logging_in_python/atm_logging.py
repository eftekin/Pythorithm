import logging
import random
import sys

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Log level can be adjusted (e.g., DEBUG, WARNING, etc.)

# Stream handler for console output
stream_handler = logging.StreamHandler(sys.stdout)
stream_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
stream_handler.setFormatter(stream_formatter)

# File handler for log file output
file_handler = logging.FileHandler("formatted.log")
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class BankAccount:
    def __init__(self, initial_balance=100):
        """
        Initialize the BankAccount with a default balance.
        Logging the account creation with the initial balance.
        """
        self.balance = initial_balance
        print("Hello! Welcome to the ATM Depot!")
        logger.info(f"BankAccount initialized with balance: {self.balance}")

    def authenticate(self, correct_pin=1234):
        """
        Authenticate the user by asking for a PIN.
        Logs invalid attempts and correct login when successful.
        """
        while True:
            try:
                pin = int(input("Enter account pin: "))
                if pin == correct_pin:
                    logger.info("User successfully authenticated.")
                    break
                else:
                    logger.error("Invalid pin entered.")
            except ValueError:
                logger.error("Non-numeric value entered for pin.")

    def deposit(self):
        """
        Deposit a valid amount into the account. Logs transactions and potential errors.
        Includes logging for:
        - Negative amounts
        - Non-numeric inputs
        - Successful deposits
        """
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount < 0:
                logger.warning(
                    "Negative amount entered for deposit. Transaction canceled."
                )
                return
            self.balance += amount
            logger.debug(
                f"Balance updated: {self.balance}"
            )  # Logging balance update for debugging
            self._log_transaction("Deposit", amount, "Successful")
        except ValueError:
            logger.error("Non-numeric value entered for deposit.")
            self._log_transaction("Deposit", None, "Failed")

    def withdraw(self):
        """
        Withdraw a valid amount if the balance permits.
        Logs transactions including:
        - Insufficient balance
        - Non-numeric inputs
        - Negative withdrawals
        """
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount < 0:
                logger.warning(
                    "Negative amount entered for withdrawal. Transaction canceled."
                )
                return
            if self.balance >= amount:
                self.balance -= amount
                logger.debug(
                    f"Balance updated: {self.balance}"
                )  # Debugging current balance after withdrawal
                self._log_transaction("Withdraw", amount, "Successful")
            else:
                logger.error(
                    "Insufficient balance for withdrawal. Transaction canceled."
                )
                self._log_transaction("Withdraw", amount, "Failed")
        except ValueError:
            logger.error("Non-numeric value entered for withdrawal.")
            self._log_transaction("Withdraw", None, "Failed")

    def display(self):
        """
        Display the current account balance.
        Includes logging for balance visibility.
        """
        print(f"\nAvailable Balance = {self.balance}")
        logger.info(f"Displayed current balance: {self.balance}")

    def _log_transaction(self, transaction_type, amount, status):
        """
        Private method to log the transaction details.
        Logs the type of transaction (Deposit or Withdraw), amount, status, and a unique transaction number.
        """
        transaction_number = random.randint(10000, 1000000)
        logger.info(f"\nTransaction Type: {transaction_type}")
        if amount is not None:
            logger.info(f"Amount: {amount}")
        logger.info(f"Status: {status}")
        logger.info(f"Transaction # {transaction_number}")


# Example usage
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
