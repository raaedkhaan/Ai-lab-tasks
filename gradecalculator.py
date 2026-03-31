marks = int(input("Enter marks (1-100): "))

if marks < 50:
    grade = 'F'
elif 50 <= marks <= 60:
    grade = 'E'
elif 61 <= marks <= 70:
    grade = 'D'
elif 71 <= marks <= 80:
    grade = 'C'
elif 81 <= marks <= 90:
    grade = 'B'
elif 91 <= marks <= 100:
    grade = 'A'
else:
    grade = "Invalid input"

print("Grade:", grade)