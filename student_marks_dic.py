Student_marks={
    "yesha":95,
    "karna":97,
    "aditi":90,
    "shikha":92,
    "bhavya":91
}

name=input("Enter your name:").lower()

if name in Student_marks:
    print(f"{name} has {Student_marks[name]} marks")
else:
    print("name is not found")
