'''
Student Name: Iqra Tahir
Roll No: PIAIC234522
Project: Student Performance Tracker
'''

# Created student class
class Student():
    def __init__(self, name):
        self.name = name
        self.scores = {} # dictionary to store scores

    def add_score(self, subject, score): # Method to add scores
        self.scores[subject] = score
        
    def calculate_average(self): # Method to calculate average
        if self.scores:
            total_score = sum(self.scores.values())
            return total_score / len(self.scores)
        else:
            return 0
    
    def has_passed(self, passing_mark=40): # Method to check it is passing score
        return self.calculate_average()>=passing_mark
        
        
    def get_performance_summary(self): # Method to get performance summary
        average = self.calculate_average()
        pass_status = 'Passed' if self.has_passed() else 'Failed'
        return {
            'name': self.name,
            'average': average,
            'pass_status': pass_status,
            'scores': self.scores
        }

# Created PerformanceTracker class
class PerformanceTracker():
    def __init__(self):
        self.students = {} # Dictionary to add students
    
    def add_student(self, student): # Method to add a student
        self.students[student.name] = student

    def calculate_class_average(self): # Method to calculate class average
        if self.students:
            total_scores = sum([student.calculate_average() for student in self.students.values()])
            return total_scores / len(self.students)
        else:
            return 0

    def display_student_performance(self): # method for display performance of students in the database 
        for student in self.students.values():
            print(student.get_performance_summary())

tracker = PerformanceTracker() # create a new PerformanceTracker object

# create and add students

student1 = Student('Alice')
student1.add_score('Math', 85)
student1.add_score('English', 90)
student1.add_score('Science', 75)

student2 = Student('Bob')
student2.add_score('Math', 90)
student2.add_score('English', 80)
student2.add_score('Science', 70)

tracker.add_student(student1)
tracker.add_student(student2)

print(tracker.display_student_performance()) # display performance of students in the database)

