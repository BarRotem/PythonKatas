def best_student(grades):
    """
    This function receives a dict of (student name -> grade) mapping, and returns the student with the highest grade
    """
    best_grade = 0
    for student, grade in grades.items():
        if grade > best_grade:
            best_grade = grade
            best_student = student
    return best_student

print(best_student({
    "Dan": 78,
    "Jessica": 88,
    "John": 99,
    "Daniel": 65,
    "Lindsy": 95
}))   # Expected John
