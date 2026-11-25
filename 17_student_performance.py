# Case Study 17: Student Performance Trend Analysis

print("STUDENT PERFORMANCE TREND")
subjects = ["Python", "Mathematics", "Physics"]
scores = [[65, 72, 80], [55, 48, 60], [40, 45, 50]]

total_marks = 0
total_scores = 0
weak_subjects = []

for i in range(len(subjects)):
    subject_total = 0
    for j in range(len(scores[i])):
        subject_total += scores[i][j]
        total_marks += scores[i][j]
        total_scores += 1

    average = subject_total / len(scores[i])
    change = scores[i][-1] - scores[i][0]
    print(subjects[i], "Average:", round(average, 2), "Change:", change)

    if average < 50:
        weak_subjects.append(subjects[i])

overall_average = total_marks / total_scores

if overall_average >= 75:
    result = "Excellent"
elif overall_average >= 60:
    result = "Good"
else:
    result = "Needs Improvement"

print("Weak Subjects:", weak_subjects)
print("Overall Average:", round(overall_average, 2))
print("Classification:", result)
