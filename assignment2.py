students = [
    {"student_id": "st101", "Student_name": "akshit", "stander": "10th", "age": 15, "Hindi": 97, "English": 89, "Maths": 85, "science": 86, "computer": 34, "total": 432},
    {"student_id": "st102", "Student_name": "Shiva", "stander": "10th", "age": 14, "Hindi": 65, "English": 45, "Maths": 48, "science": 90, "computer": 45, "total": 313},
    {"student_id": "st103", "Student_name": "Shrub", "stander": "10th", "age": 16, "Hindi": 23, "English": 48, "Maths": 45, "science": 90, "computer": 90, "total": 423},
    {"student_id": "st104", "Student_name": "Ruby", "stander": "10th", "age": 14, "Hindi": 45, "English": 67, "Maths": 45, "science": 45, "computer": 56, "total": 258},
    {"student_id": "st105", "Student_name": "Aman", "stander": "10th", "age": 15, "Hindi": 78, "English": 88, "Maths": 92, "science": 81, "computer": 72, "total": 411},
    {"student_id": "st106", "Student_name": "Kavya", "stander": "10th", "age": 15, "Hindi": 82, "English": 79, "Maths": 85, "science": 84, "computer": 88, "total": 418},
    {"student_id": "st107", "Student_name": "Arjun", "stander": "10th", "age": 14, "Hindi": 90, "English": 94, "Maths": 97, "science": 85, "computer": 77, "total": 443},
    {"student_id": "st108", "Student_name": "Meera", "stander": "10th", "age": 14, "Hindi": 65, "English": 75, "Maths": 80, "science": 88, "computer": 90, "total": 398},
    {"student_id": "st109", "Student_name": "Nina", "stander": "10th", "age": 16, "Hindi": 55, "English": 50, "Maths": 60, "science": 70, "computer": 68, "total": 303},
    {"student_id": "st110", "Student_name": "Rahul", "stander": "10th", "age": 15, "Hindi": 70, "English": 60, "Maths": 78, "science": 82, "computer": 85, "total": 375}
]


print("The name of students who have marks more then 50 in English: ")
for student in students:
    english = student["English"]
    if english > 50:
        print(student["Student_name"], end=", ")
   
   
   