print("=== Student Grade Calculator ===")

name = input("Enter student name: ")
prelim = float(input("Enter Prelim grade: "))
midterm = float(input("Enter Midterm grade: "))
final = float(input("Enter Final grade: "))

average = (prelim + midterm + final) / 3

print("\n=== Grade Result ===")
print("Student:", name)
print("Average:", round(average, 2))

if average >= 90:
    remarks = "Excellent"
elif average >= 85:
    remarks = "Very Good"
elif average >= 75:
    remarks = "Passed"
else:
    remarks = "Failed"

print("Remarks:", remarks)