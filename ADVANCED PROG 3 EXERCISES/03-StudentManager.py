import tkinter as tk
from tkinter import ttk, messagebox
import os

class Student:
    def __init__(self, code, name, course_marks, exam_mark):
        self.code = code
        self.name = name
        self.course_marks = course_marks
        self.exam_mark = exam_mark
        self.total_score = sum(course_marks) + exam_mark
        self.percentage = (self.total_score / 160) * 100
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 70: return 'A'
        elif self.percentage >= 60: return 'B'
        elif self.percentage >= 50: return 'C'
        elif self.percentage >= 40: return 'D'
        else: return 'F'

    def display_record(self):
        return f"Name: {self.name}\nStudent Number: {self.code}\n" \
               f"Total Coursework Mark: {sum(self.course_marks)}\n" \
               f"Exam Mark: {self.exam_mark}\n" \
               f"Overall Percentage: {self.percentage:.2f}%\n" \
               f"Grade: {self.grade}"

def load_students(filename):
    students = []
    with open(filename, 'r') as file:
        num_students = int(file.readline().strip())
        for _ in range(num_students):
            line = file.readline().strip().split(',')
            code = int(line[0])
            name = line[1].strip()
            course_marks = [int(mark) for mark in line[2:5]]
            exam_mark = int(line[5])
            students.append(Student(code, name, course_marks, exam_mark))
    return students

class StudentManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Manager")
        self.master.geometry("600x400")
        
        self.students = load_students("studentMarks.txt")
        
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Student Manager", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        ttk.Button(button_frame, text="View All Records", command=self.view_all_records).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Show Highest Score", command=self.show_highest_score).grid(row=0, column=1, padx=10)
        ttk.Button(button_frame, text="Show Lowest Score", command=self.show_lowest_score).grid(row=0, column=2, padx=10)

        ttk.Button(self.master, text="View Individual Record", command=self.view_individual_record).pack(pady=10)
        
        self.result_text = tk.Text(self.master, height=15, width=70)
        self.result_text.pack(pady=10)

    def view_all_records(self):
        self.result_text.delete(1.0, tk.END)
        for student in self.students:
            self.result_text.insert(tk.END, student.display_record() + "\n\n")
        
        avg_percentage = sum(student.percentage for student in self.students) / len(self.students)
        summary = f"Number of students: {len(self.students)}\n"
        summary += f"Average percentage mark: {avg_percentage:.2f}%"
        self.result_text.insert(tk.END, summary)

    def view_individual_record(self):
        names = [student.name for student in self.students]
        student_window = tk.Toplevel(self.master)
        student_window.title("Select a Student")
        
        listbox = tk.Listbox(student_window)
        listbox.pack(padx=10, pady=10)
        
        for name in names:
            listbox.insert(tk.END, name)
        
        def on_select():
            selection = listbox.curselection()
            if selection:
                index = selection[0]
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, self.students[index].display_record())
                student_window.destroy()
        
        ttk.Button(student_window, text="Select", command=on_select).pack(pady=10)

    def show_highest_score(self):
        highest_student = max(self.students, key=lambda x: x.total_score)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Student with highest overall mark:\n\n")
        self.result_text.insert(tk.END, highest_student.display_record())

    def show_lowest_score(self):
        lowest_student = min(self.students, key=lambda x: x.total_score)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Student with lowest overall mark:\n\n")
        self.result_text.insert(tk.END, lowest_student.display_record())

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()