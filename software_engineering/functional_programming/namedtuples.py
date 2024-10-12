from collections import namedtuple

# Define a namedtuple for countries
Country = namedtuple("Country", ["name", "capital", "continent"])

# Create instances of the namedtuple
usa = Country("United States", "Washington D.C.", "North America")
france = Country("France", "Paris", "Europe")
japan = Country("Japan", "Tokyo", "Asia")

countries = (usa, france, japan)

# Example of accessing values
for country in countries:
    print(f"{country.name} is in {country.continent} with capital {country.capital}")
