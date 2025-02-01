'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Assignment: Student Database Management
'''

def manage_student_database():  #created function to manage database of students
    students : list = [] # created empty list
    student_id = 1
    while True: #loop to add students
     student_name = input(f'Enter student name for student ID {student_id}  or enter "stop" to quit: ')
     if student_name.lower() == "stop":
        break
     if any(student[1] == student_name for student in students):
      print("Duplicate name detected! Please enter a unique name.")
     else:
        student = (student_id, student_name)
        students.append(student)
        student_id += 1
    print("Student list:")
    for student in students: #print student info
        print(f"ID: {student[0]}, Student Name: {student[1]}")
    print(f"\nTotal number of students: {len(students)}")    # total number of students
    total_name_length = sum(len(student[1]) for student in students)    # total length of students names
    print(f"Total length of all student names combined: {total_name_length}")
    if students:
     longest_name_student = max(students, key=lambda student: len(student[1])) #finding the longest student name
     print(f"\nStudent with the longest name: ID: {longest_name_student[0]}, Name: {longest_name_student[1]} (Length: {len(longest_name_student[1])})")
     shortest_name_student = min(students, key=lambda student: len(student[1])) #finding the shortest student name
     print(f"Student with the shortest name: ID: {shortest_name_student[0]}, Name: {shortest_name_student[1]} (Length: {len(shortest_name_student[1])})")
manage_student_database()


