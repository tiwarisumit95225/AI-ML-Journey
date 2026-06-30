import numpy as np

# ==================================================
#              STUDENT MARKS ANALYZER
# ==================================================

names = np.array(["Aman", "Rahul", "Sumit", "Priya", "Anjali", "Rohit"])
marks = np.array([85, 92, 78, 95, 88, 67])

def heading(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

# ==================================================
# Student Records
# ==================================================
heading("Student Records")


for i in range(len(names)):
    print(f"{names[i]:<12}: {marks[i]:>3}")

# ==================================================
# Statistics
# ==================================================

heading("Statistics")

total_students = len(names)
total_marks = np.sum(marks)
average_marks = np.mean(marks)
highest_marks = np.max(marks)
lowest_marks = np.min(marks)
median_marks = np.median(marks)
standard_deviation = np.std(marks)

print(f"{'Total Students':<22}: {total_students}")
print(f"{'Total Marks':<22}: {total_marks}")
print(f"{'Average Marks':<22}: {average_marks:.2f}")
print(f"{'Highest Marks':<22}: {highest_marks}")
print(f"{'Lowest Marks':<22}: {lowest_marks}")
print(f"{'Median Marks':<22}: {median_marks:.2f}")
print(f"{'Standard Deviation':<22}: {standard_deviation:.2f}")

# ==================================================
# Topper
# ==================================================
heading("Topper")
topper_index = np.argmax(marks)



print(f"{names[topper_index]:<12}: {marks[topper_index]}")

# ==================================================
# Students Scoring Above 90
# ==================================================
heading("Students Scoring Above 90")


mask = marks > 90

top_students = names[mask]
top_marks = marks[mask]

for i in range(len(top_students)):
    print(f"{top_students[i]:<12}: {top_marks[i]}")

# ==================================================
# Grading System
# ==================================================
heading("Grading System")


for i in range(len(names)):
    curr_marks = marks[i]

    if curr_marks >= 90:
        grade = "A"
    elif curr_marks >= 80:
        grade = "B"
    elif curr_marks >= 70:
        grade = "C"
    elif curr_marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{names[i]:<12}: {grade}")

# ==================================================
# Pass / Fail
# ==================================================
heading("Pass / Fail")


for i in range(len(names)):
    status = "Pass" if marks[i] >= 40 else "Fail"
    print(f"{names[i]:<12}: {status}")

# ==================================================
# Student Ranking
# ==================================================
heading("Student Ranking")


sorted_index = np.argsort(marks)[::-1]

for i in range(len(names)):
    print(f"{i+1}. {names[sorted_index[i]]:<10} : {marks[sorted_index[i]]:>3}")

# ==================================================
# Top 3 Students
# ==================================================
heading("Top 3 Students")


for i in range(3):
    print(f"{i+1}. {names[sorted_index[i]]:<10} : {marks[sorted_index[i]]:>3}")
    
# ==================================================
#           Student Below  Average
# ==================================================
heading("Student Below  Average")

mask2=marks<average_marks
below_average_marks=marks[mask2]
below_average_student=names[mask2]

for i in range(len(below_average_marks)):
   print(f"{below_average_student[i]:<10} : {below_average_marks[i]:>3}")

# ==================================================
#           Grade Distribution
# ==================================================
heading("Grade Distribution")

grade_a = np.sum(marks >= 90)
grade_b = np.sum((marks >= 80) & (marks < 90))
grade_c = np.sum((marks >= 70) & (marks < 80))
grade_d = np.sum((marks >= 60) & (marks < 70))
grade_f = np.sum(marks < 60)

print(f"{'Grade A':<20}: {grade_a}")
print(f"{'Grade B':<20}: {grade_b}")
print(f"{'Grade C':<20}: {grade_c}")
print(f"{'Grade D':<20}: {grade_d}")
print(f"{'Grade F':<20}: {grade_f}")

# ==================================================
#                PASS PERCENTAGE
# ==================================================
heading("PASS PERCENTAGE")

pass_student=np.sum(marks>=40)
fail_student=np.sum(marks<40)

print(f"{'Passed Students':<20} : {pass_student}")
print(f"{'Failed Students':<20} : {fail_student}")

pass_percentage = (pass_student / len(names)) * 100

print(f"{'Pass Percentage':<20} : {pass_percentage:.2f}%")
