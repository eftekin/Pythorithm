class School:
    def __init__(self, name, level, numberOfStudents):
        """Constructor for the School class. Initializes the school's name, level, and number of students."""
        self._name = name
        self._level = level
        self._numberOfStudents = numberOfStudents

    # Getter and setter methods using property for cleaner syntax
    @property
    def name(self):
        """Returns the name of the school."""
        return self._name

    @property
    def level(self):
        """Returns the level of the school (e.g., primary, high)."""
        return self._level

    @property
    def numberOfStudents(self):
        """Returns the current number of students."""
        return self._numberOfStudents

    @numberOfStudents.setter
    def numberOfStudents(self, newNumberOfStudents):
        """Sets a new number of students for the school."""
        self._numberOfStudents = newNumberOfStudents

    def __repr__(self):
        """Returns a string representation of the school."""
        return f"A {self._level} school named {self._name} with {self._numberOfStudents} students"


# Example usage of the School class
school1 = School("Harvard-Westlake", "high", 1000)

# Accessing properties (formerly getter methods)
print(school1.name)  # Output: Harvard-Westlake
print(school1.level)  # Output: high
print(school1.numberOfStudents)  # Output: 1000

# Updating the number of students using the setter
school1.numberOfStudents = 1200

# Checking the updated value
print(school1.numberOfStudents)  # Output: 1200

# Displaying the full representation of the object
print(school1)  # Output: A high school named Harvard-Westlake with 1200 students


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        """Constructor for the PrimarySchool class. Adds pickup policy attribute."""
        super().__init__(name, "primary", numberOfStudents)
        self._pickupPolicy = pickupPolicy

    @property
    def pickupPolicy(self):
        """Returns the pickup policy of the primary school."""
        return self._pickupPolicy

    def __repr__(self):
        """Returns a string representation of the primary school, including pickup policy."""
        parentRepr = super().__repr__()
        return f"{parentRepr}. The pickup policy is {self._pickupPolicy}"


# Example usage of the PrimarySchool class
primarySchool1 = PrimarySchool("PS 321", 600, "Pickup Allowed")

# Accessing the pickup policy property
print(primarySchool1.pickupPolicy)  # Output: Pickup Allowed

# Displaying the full representation of the object
print(primarySchool1)
# Output: A primary school named PS 321 with 600 students. The pickup policy is Pickup Allowed


class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        """Constructor for the HighSchool class. Adds sports teams attribute."""
        super().__init__(name, "high", numberOfStudents)
        self._sportsTeams = sportsTeams

    @property
    def sportsTeams(self):
        """Returns the list of sports teams in the high school."""
        return self._sportsTeams

    def __repr__(self):
        """Returns a string representation of the high school, including sports teams."""
        parentRepr = super().__repr__()
        return f"{parentRepr}. The sports teams are {', '.join(self._sportsTeams)}"


# Example usage of the HighSchool class
highSchool1 = HighSchool("Bronx Science", 3200, ["Soccer", "Basketball", "Tennis"])

# Accessing the sports teams property
print(highSchool1.sportsTeams)  # Output: ['Soccer', 'Basketball', 'Tennis']

# Displaying the full representation of the object
print(highSchool1)
# Output: A high school named Bronx Science with 3200 students. The sports teams are Soccer, Basketball, Tennis
