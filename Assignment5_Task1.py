try:
    student_marks = {"JHON":84, "HARRY":78, "PETER":98, "SAM":54}
    user = input("Enter your name: ")
    upper_user = user.upper()
    print(f"{upper_user} obtain marks: {student_marks[upper_user]}")

except KeyError:
    print("Student not found")

