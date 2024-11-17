import random

import pandas as pd
from faker import Faker

# Initialize the Faker library
faker = Faker()


# Function to generate fake student data
def generate_student_data(num_students=500):
    data = {
        "Name": [],
        "Surname": [],
        "ID": [],
        "Physics": [],
        "Calculus": [],
        "Advanced Programming": [],
        "Chemistry": [],
    }

    for _ in range(num_students):
        data["Name"].append(faker.first_name())
        data["Surname"].append(faker.last_name())
        data["ID"].append(faker.unique.random_int(min=1000, max=9999))
        data["Physics"].append(
            random.randint(50, 100)
        )  # Random score between 50 and 100
        data["Calculus"].append(random.randint(50, 100))
        data["Advanced Programming"].append(random.randint(50, 100))
        data["Chemistry"].append(random.randint(50, 100))

    return pd.DataFrame(data)


# Generate 200 fake student records
fake_student_data = generate_student_data(num_students=200)

# Save to Excel file
file_path = "./student_data.xlsx"
fake_student_data.to_excel(file_path, index=False)

file_path
