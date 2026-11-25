# Case Study 12: Attendance Recovery Computation

print("ATTENDANCE RECOVERY")
attended = 72
total = 100
required = 75

percentage = attended / total * 100
print("Current Attendance:", round(percentage, 2), "%")

extra_classes = 0
while percentage < required:
    attended = attended + 1
    total = total + 1
    extra_classes = extra_classes + 1
    percentage = attended / total * 100

print("Minimum Additional Classes Required:", extra_classes)
print("Attendance After Recovery:", round(percentage, 2), "%")
