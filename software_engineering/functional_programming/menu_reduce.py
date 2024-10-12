from collections import namedtuple
from functools import reduce

# Define a namedtuple for menu items
MenuItem = namedtuple("MenuItem", ["name", "dish_type", "price"])

# Create menu items
menu = (
    MenuItem("Jumbo Shrimp Platter", "Appetizer", 29.95),
    MenuItem("Lobster Cake", "Appetizer", 30.95),
    MenuItem("Ribeye Steak", "Entree", 75.95),
    MenuItem("Caeser Salad", "Salad", 14.95),
    MenuItem("Mashed Potatoes", "Side", 14.95),
)

# Find the most expensive entree
most_expensive_entree = reduce(
    lambda x, y: x if x.price > y.price else y,
    filter(lambda x: x.dish_type == "Entree", menu),
)

print(
    most_expensive_entree
)  # Output: MenuItem(name='Ribeye Steak', dish_type='Entree', price=75.95)
