# Input
name = input("Enter your name: ")
science = int(input("Enter your science marks: "))
maths = int(input("Enter your maths marks: "))
english = int(input("Enter your english marks: "))
hindi = int(input("Enter your hindi marks: "))

# Lambda for average calculation
averageFinder = lambda a, b, c, d: (a + b + c + d) // 4

# Calculate average
average = averageFinder(science, maths, english, hindi)

# Grade assignment
if average >= 80:
    grade = 'A'
elif average > 60:
    grade = 'B'
elif average > 35:
    grade = 'C'
else:
    grade = 'D'

# Create the student dictionary
students = [
    {
        "name": name,
        "marks": {
            "science": science,
            "maths": maths,
            "english": english,
            "hindi": hindi,
        },
        "average": average,
        "grade": grade,
    }
]

# Output
print(students)
