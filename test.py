import streamlit as st
import pandas as pd
from datetime import datetime


class Student():
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, subject, score):
        # Automatically capture the current date
        test_date = datetime.now().strftime("%Y-%m-%d")
        # Store subject and date as a key, and score as value
        self.scores[(subject, test_date)] = score
        
    def calculate_average(self):
        if self.scores:
            total_score = sum(score for (subject, date), score in self.scores.items())
            return total_score / len(self.scores)
        else:
            return 0
    
    def has_passed(self, passing_mark=50):
        return self.calculate_average()>=passing_mark
        
        
    def get_performance_summary(self):
        average = self.calculate_average()
        pass_status = 'Passed' if self.has_passed() else 'Failed'
        return {
            'name': self.name,
            'average': average,
            'pass_status': pass_status,
            'scores': self.scores,
        }

class PerformanceTracker():
    def __init__(self):
        self.students = {}
    
    def add_student(self, student):
        self.students[student.name] = student

    def get_student(self, name):
        return self.students.get(name)

    def calculate_class_average(self):
        if self.students:
            total_scores = sum([student.calculate_average() for student in self.students.values()])
            return total_scores / len(self.students)
        else:
            return 0

    def display_student_performance(self):
        data=[]
        for student in self.students.values():
            summary = student.get_performance_summary()
            for (subject, test_date), score in summary['scores'].items():
                data.append({
                    'Student Name': summary['name'],
                    'Subject': subject,
                    'Score': score,
                    'Average Score': summary['average'],
                    'Pass Status': summary['pass_status'],
                    'Date': test_date
                    })
        return pd.DataFrame(data) if data else pd.DataFrame(columns=['Student Name', 'Subject', 'Score', 'Average Score', 'Pass Status','Date'])


tracker = PerformanceTracker()

st.title("Student Performance Tracker")

# Initialize the tracker in session state if it doesn't already exist
if 'tracker' not in st.session_state:
    st.session_state.tracker = PerformanceTracker()

if 'num_subjects' not in st.session_state:
    st.session_state.num_subjects = 1

# Initialize subjects and scores in session state
if 'subjects' not in st.session_state:
    st.session_state.subjects = []
if 'scores' not in st.session_state:
    st.session_state.scores = {}

# Admin Mode for adding student performance
def admin_mode():
    st.title("Admin - Add Student Performance")

    # Input for student name
    student_name = st.text_input("Student Name")

    # Dynamic section to add multiple subjects and scores
    num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=10, value=st.session_state.num_subjects)
    st.session_state.num_subjects = num_subjects  # Save the number of subjects to session state

    subjects = []
    scores = []

    # Create inputs for each subject and corresponding score
    for i in range(num_subjects):
        subject = st.text_input(f"Subject {i + 1}")
        score = st.number_input(f"Score {i + 1}", min_value=0, max_value=100, step=1)
        subjects.append(subject)
        scores.append(score)

    if st.button("Add Performance"):
        if student_name and all(subjects) and all(scores):
            # Fetch the student or create a new one if not found
            student = st.session_state.tracker.get_student(student_name)
            if not student:
                student = Student(student_name)
                st.session_state.tracker.add_student(student)

            # Add all subjects and their scores to the student
            for subject, score in zip(subjects, scores):
                student.add_score(subject, score)
            
            st.success(f"Added performance for {student_name}.")
        else:
            st.error("Please fill out all fields (student name, subjects, and scores).")

# Display all students' performance using pandas
    st.subheader("All Students' Performance")
    df = st.session_state.tracker.display_student_performance()
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No data available yet.")

# Student Mode for viewing personal performance
def student_mode():
    st.title("Student - View Your Performance")

    student_name = st.text_input("Enter your name")

    if student_name:
        student = st.session_state.tracker.get_student(student_name)
        if student:
            # Create a DataFrame for student-specific data
            performance_summary = student.get_performance_summary()
            scores_df = pd.DataFrame({
                'Subject': list(performance_summary['scores'].keys()),
                'Score': list(performance_summary['scores'].values()),
                'Date': [date for (subject, date) in performance_summary['scores'].keys()]

            })
            st.subheader(f"Performance Summary for {student_name}")
            st.write(f"Average Score: {performance_summary['average']:.2f}")
            st.write(f"Status: {performance_summary['pass_status']}")
            st.table(scores_df)
        else:
            st.warning(f"No performance data found for {student_name}.")

# Main function for handling modes
def main():
    st.sidebar.title("Select Mode")
    mode = st.sidebar.selectbox("Choose a mode", ["Admin", "Student"])

    if mode == "Admin":
        admin_mode()
    elif mode == "Student":
        student_mode()

if __name__ == "__main__":
    main()