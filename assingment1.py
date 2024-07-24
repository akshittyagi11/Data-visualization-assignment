row_1 = ["student_id", "Student_name", "stander", "age", "Hindi", "English", "Maths", "science", "computer", "total"]
row_2 = ["st101", "Akhit", "10th", 15, 97, 89, 85, 86, 34, 432]
row_3 = ["st102", "Shivam", "10th", 14, 65, 45, 48, 90, 45, 313]
row_4 = ["st103", "Nitin", "10th", 16, 23, 48, 45, 90, 90, 423]
row_5 = ["st104", "Ruby", "10th", 14, 45, 67, 45, 45, 56, 258]
row_6 = ["st105", "Aman", "10th", 15, 78, 88, 92, 81, 72, 411]
row_7 = ["st106", "Kavya", "10th", 15, 82, 79, 85, 84, 88, 418]
row_8 = ["st107", "Arjun", "10th", 14, 90, 94, 97, 85, 77, 443]
row_9 = ["st108", "Meera", "10th", 14, 65, 75, 80, 88, 90, 398]
row_10 = ["st109", "Nina", "10th", 16, 55, 50, 60, 70, 68, 303]
row_11 = ["st110", "Rahul", "10th", 15, 70, 60, 78, 82, 85, 375]

final_record = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11]

# Display the names of students whose marks in English are greater than 60
print("The names of students whose marks in English are greater than 60 are:")
for row in range(1, len(final_record)):
    if final_record[row][5] > 60:
        print(final_record[row][1], end=", ")

# Display the top 4 students who topped in Maths
print("\nThe name and age of the top 4 students who topped in Maths:")
maths_marks = [(final_record[row][6], row) for row in range(1, len(final_record))]
sorted_maths_marks = sorted(maths_marks, reverse=True)
# Get the top 4 students
top_4 = sorted_maths_marks[:4]
# Print the name and age of the top 4 students
for mark, row in top_4:
    print(f"Name: {final_record[row][1]}, Age: {final_record[row][3]}")

# Display the ID and age of students who are bottom 3 of the class based on total marks
print("\nThe ID and age of the students who are bottom 3 of the class based on total marks:")
total_marks = [(final_record[row][9], row) for row in range(1, len(final_record))]
sorted_total_marks = sorted(total_marks)
# Get the bottom 3 students
bottom_3 = sorted_total_marks[:3]

# Print the ID and age of the bottom 3 students
for mark, row in bottom_3:
    print(f"ID: {final_record[row][0]}, Age: {final_record[row][3]}")
  

