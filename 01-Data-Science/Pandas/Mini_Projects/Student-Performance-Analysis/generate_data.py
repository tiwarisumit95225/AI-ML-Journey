import pandas as pd
import random
from faker import Faker

fake=Faker("en_IN")
branches = ["CSE", "IT", "EC", "ME"]

cities = [
    "Indore",
    "Bhopal",
    "Delhi",
    "Mumbai",
    "Pune",
    "Jaipur",
    "Lucknow",
    "Patna",
    "Nagpur",
    "Hyderabad"
]

genders = ["Male", "Female"]
students = []

for i in range(200):
    student = {
        "Student_ID": 1001 + i,
        "Name": fake.name(),
        "Gender": random.choice(genders),
        "Age": random.randint(18, 24),
        "Branch": random.choice(branches),
        "Semester": random.randint(1, 8),
        "Math": random.randint(30, 100),
        "Physics": random.randint(30, 100),
        "Chemistry": random.randint(30, 100),
        "English": random.randint(30, 100),
        "Attendance": random.randint(50, 100),
        "City": random.choice(cities)
    }
    students.append(student)

df=pd.DataFrame(students)

df.to_csv("data/students.csv", index=False)

print("Dataset generated successfully!")