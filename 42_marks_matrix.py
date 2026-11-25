# Case Study 42: Student Marks Matrix Analysis

print("STUDENT MARKS MATRIX ANALYSIS")
students = ["Asha", "Balu", "Charan", "Divya"]
subjects = ["Python", "Maths", "Physics"]
marks = [
    [85, 78, 90],
    [65, 72, 68],
    [40, 45, 50],
    [92, 88, 95]
]

top_total = -1
top_student = ""

for i in range(len(students)):
    total = 0
    for j in range(len(subjects)):
        total += marks[i][j]

    average = total / len(subjects)
    print(students[i], "Total:", total, "Average:", round(average, 2))

    if total > top_total:
        top_total = total
        top_student = students[i]

low_subjects = []
for j in range(len(subjects)):
    subject_total = 0
    for i in range(len(students)):
        subject_total += marks[i][j]

    subject_average = subject_total / len(students)
    print(subjects[j], "Average:", round(subject_average, 2))

    if subject_average < 50:
        low_subjects.append(subjects[j])

print("Top Performer:", top_student, "with", top_total, "marks")
print("Low-Average Subjects:", low_subjects)
