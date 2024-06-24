
import tkinter as tk
from tkinter import ttk  # Import ttk from tkinter for themed widgets
from tkinter import messagebox
import mysql.connector

# Rest of your code follows...


# Function to establish database connection
def connect_to_database():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Kach@#$123",
            database="eduschema"
        )
        return db, db.cursor()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        return None, None

# Function to add a course
def add_course():
    try:
        course_id = int(course_id_entry.get())
        course_name = course_name_entry.get()
        course_description = course_description_entry.get()
        course_duration = int(course_duration_entry.get())
        course_category = course_category_entry.get()
        course_level = course_level_entry.get()
        course_status = 'Active'

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "INSERT INTO Courses (course_id, course_name, course_description, course_duration, course_category, course_level, course_status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (course_id, course_name, course_description, course_duration, course_category, course_level, course_status)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Course added successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid course duration value. Please enter a valid integer.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error adding course: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to update a course
def update_course():
    try:
        course_id = int(course_id_entry.get())
        course_name = course_name_entry.get()
        course_description = course_description_entry.get()
        course_duration = int(course_duration_entry.get())
        course_category = course_category_entry.get()
        course_level = course_level_entry.get()

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "UPDATE Courses SET course_name=%s, course_description=%s, course_duration=%s, course_category=%s, course_level=%s WHERE course_id=%s"
        values = (course_name, course_description, course_duration, course_category, course_level, course_id)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Course updated successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid course duration value. Please enter a valid integer.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error updating course: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to remove a course
def remove_course():
    try:
        course_id = int(course_id_entry.get())

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "UPDATE Courses SET course_status = 'Inactive' WHERE course_id = %s"
        cursor.execute(sql, (course_id,))
        db.commit()

        log_deleted_record('Courses', course_id)
        messagebox.showinfo("Success", "Course removed successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid course ID. Please enter a valid integer.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error removing course: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to add an instructor
def add_instructor():
    try:
        instructor_name = instructor_name_entry.get()
        instructor_email = instructor_email_entry.get()
        instructor_bio = instructor_bio_entry.get()
        specialization_area = specialization_area_entry.get()

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "INSERT INTO Instructors (instructor_name, instructor_email, instructor_bio, specialization_area) VALUES (%s, %s, %s, %s)"
        values = (instructor_name, instructor_email, instructor_bio, specialization_area)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Instructor added successfully.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error adding instructor: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to update an instructor
def update_instructor():
    try:
        instructor_id = int(instructor_id_entry.get())
        instructor_name = instructor_name_entry.get()
        instructor_email = instructor_email_entry.get()
        instructor_bio = instructor_bio_entry.get()
        specialization_area = specialization_area_entry.get()

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "UPDATE Instructors SET instructor_name=%s, instructor_email=%s, instructor_bio=%s, specialization_area=%s WHERE instructor_id=%s"
        values = (instructor_name, instructor_email, instructor_bio, specialization_area, instructor_id)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Instructor updated successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid instructor ID. Please enter a valid integer.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error updating instructor: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to delete an instructor
def delete_instructor():
    try:
        instructor_id = int(instructor_id_entry.get())

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "UPDATE Instructors SET instructor_status='Inactive' WHERE instructor_id=%s"
        cursor.execute(sql, (instructor_id,))
        db.commit()

        log_deleted_record('Instructors', instructor_id)
        messagebox.showinfo("Success", "Instructor deleted successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid instructor ID. Please enter a valid integer.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error deleting instructor: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to enroll a student in a course
def enroll_student():
    try:
        student_id = int(student_id_entry.get())
        course_id = int(course_id_entry_enroll.get())

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "INSERT INTO Enrollments (student_id, course_id) VALUES (%s, %s)"
        values = (student_id, course_id)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Student enrolled successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid student or course ID. Please enter valid integers.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error enrolling student: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to create an assessment for a course
def create_assessment():
    try:
        course_id = int(course_id_entry_assessment.get())
        assessment_name = assessment_name_entry.get()
        assessment_date = assessment_date_entry.get()
        total_marks = int(total_marks_entry.get())

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "INSERT INTO Assessments (course_id, assessment_name, assessment_date, total_marks) VALUES (%s, %s, %s, %s)"
        values = (course_id, assessment_name, assessment_date, total_marks)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Assessment created successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid course ID or total marks. Please enter valid integers.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error creating assessment: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to record a grade for a student in an assessment
def record_grade():
    try:
        assessment_id = int(assessment_id_entry.get())
        student_id = int(student_id_entry_grade.get())
        obtained_marks = float(obtained_marks_entry.get())

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "INSERT INTO Grades (assessment_id, student_id, obtained_marks) VALUES (%s, %s, %s)"
        values = (assessment_id, student_id, obtained_marks)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Grade recorded successfully.")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid assessment ID, student ID, or obtained marks. Please enter valid values.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error recording grade: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

def show_recently_deleted():
    try:
        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "SELECT deleted_table, deleted_record_id FROM recently_deleted"
        cursor.execute(sql)
        results = cursor.fetchall()

        if not results:
            messagebox.showinfo("Info", "No recently deleted records.")
            return

        # Create a new window to display recently deleted records
        deleted_records_window = tk.Toplevel(root)
        deleted_records_window.title("Recently Deleted Records")

        # Display table headers
        tk.Label(deleted_records_window, text="Table Name").grid(row=0, column=0)
        tk.Label(deleted_records_window, text="Record ID").grid(row=0, column=1)

        # Display deleted records
        for index, (table_name, record_id) in enumerate(results, start=1):
            tk.Label(deleted_records_window, text=table_name).grid(row=index, column=0)
            tk.Label(deleted_records_window, text=str(record_id)).grid(row=index, column=1)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error fetching deleted records: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to view a student's grades
def view_grades():
    try:
        student_id = int(student_id_entry_view_grades.get())

        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "SELECT Assessments.assessment_name, Grades.obtained_marks, Assessments.total_marks FROM Grades JOIN Assessments ON Grades.assessment_id = Assessments.assessment_id WHERE Grades.student_id = %s"
        cursor.execute(sql, (student_id,))
        results = cursor.fetchall()

        grades_window = tk.Toplevel(root)
        grades_window.title("Student Grades")

        for index, (assessment_name, obtained_marks, total_marks) in enumerate(results):
            tk.Label(grades_window, text=f"Assessment: {assessment_name}").grid(row=index, column=0)
            tk.Label(grades_window, text=f"Obtained Marks: {obtained_marks} / {total_marks}").grid(row=index, column=1)

    except ValueError:
        messagebox.showerror("Input Error", "Invalid student ID. Please enter a valid integer.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error viewing grades: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Function to log a recently deleted record
def log_deleted_record(table_name, record_id):
    try:
        db, cursor = connect_to_database()
        if db is None or cursor is None:
            return

        sql = "INSERT INTO recently_deleted (deleted_table, deleted_record_id) VALUES (%s, %s)"
        values = (table_name, record_id)
        cursor.execute(sql, values)
        db.commit()
        messagebox.showinfo("Success", "Deleted record logged successfully.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error logging deleted record: {err}")
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

# Setting up the main window
root = tk.Tk()
root.title("EduSchema Management System")

# Creating tabs for each function
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, columnspan=4, rowspan=6)

# Frames for each tab
course_frame = tk.Frame(notebook)
instructor_frame = tk.Frame(notebook)
enrollment_frame = tk.Frame(notebook)
assessment_frame = tk.Frame(notebook)
grade_frame = tk.Frame(notebook)
view_grades_frame = tk.Frame(notebook)

course_frame.grid(row=0, column=0)
instructor_frame.grid(row=0, column=1)
enrollment_frame.grid(row=0, column=2)
assessment_frame.grid(row=0, column=3)
grade_frame.grid(row=0, column=4)
view_grades_frame.grid(row=0, column=5)

notebook.add(course_frame, text='Courses')
notebook.add(instructor_frame, text='Instructors')
notebook.add(enrollment_frame, text='Enrollments')
notebook.add(assessment_frame, text='Assessments')
notebook.add(grade_frame, text='Grades')
notebook.add(view_grades_frame, text='View Grades')

# Labels and Entries for Courses Tab
tk.Label(course_frame, text="Course ID").grid(row=0, column=0)
course_id_entry = tk.Entry(course_frame)
course_id_entry.grid(row=0, column=1)

tk.Label(course_frame, text="Course Name").grid(row=1, column=0)
course_name_entry = tk.Entry(course_frame)
course_name_entry.grid(row=1, column=1)

tk.Label(course_frame, text="Course Description").grid(row=2, column=0)
course_description_entry = tk.Entry(course_frame)
course_description_entry.grid(row=2, column=1)

tk.Label(course_frame, text="Course Duration (in months)").grid(row=3, column=0)
course_duration_entry = tk.Entry(course_frame)
course_duration_entry.grid(row=3, column=1)

tk.Label(course_frame, text="Course Category").grid(row=4, column=0)
course_category_entry = tk.Entry(course_frame)
course_category_entry.grid(row=4, column=1)

tk.Label(course_frame, text="Course Level").grid(row=5, column=0)
course_level_entry = tk.Entry(course_frame)
course_level_entry.grid(row=5, column=1)

tk.Button(course_frame, text="Add Course", command=add_course).grid(row=6, column=0)
tk.Button(course_frame, text="Update Course", command=update_course).grid(row=6, column=1)
tk.Button(course_frame, text="Remove Course", command=remove_course).grid(row=6, column=2)

# Labels and Entries for Instructors Tab
tk.Label(instructor_frame, text="Instructor ID").grid(row=0, column=0)
instructor_id_entry = tk.Entry(instructor_frame)
instructor_id_entry.grid(row=0, column=1)

tk.Label(instructor_frame, text="Instructor Name").grid(row=1, column=0)
instructor_name_entry = tk.Entry(instructor_frame)
instructor_name_entry.grid(row=1, column=1)

tk.Label(instructor_frame, text="Instructor Email").grid(row=2, column=0)
instructor_email_entry = tk.Entry(instructor_frame)
instructor_email_entry.grid(row=2, column=1)

tk.Label(instructor_frame, text="Instructor Bio").grid(row=3, column=0)
instructor_bio_entry = tk.Entry(instructor_frame)
instructor_bio_entry.grid(row=3, column=1)

tk.Label(instructor_frame, text="Specialization Area").grid(row=4, column=0)
specialization_area_entry = tk.Entry(instructor_frame)
specialization_area_entry.grid(row=4, column=1)

tk.Button(instructor_frame, text="Add Instructor", command=add_instructor).grid(row=5, column=0)
tk.Button(instructor_frame, text="Update Instructor", command=update_instructor).grid(row=5, column=1)
tk.Button(instructor_frame, text="Delete Instructor", command=delete_instructor).grid(row=5, column=2)

# Labels and Entries for Enrollments Tab
tk.Label(enrollment_frame, text="Student ID").grid(row=0, column=0)
student_id_entry = tk.Entry(enrollment_frame)
student_id_entry.grid(row=0, column=1)

tk.Label(enrollment_frame, text="Course ID").grid(row=1, column=0)
course_id_entry_enroll = tk.Entry(enrollment_frame)
course_id_entry_enroll.grid(row=1, column=1)

tk.Button(enrollment_frame, text="Enroll Student", command=enroll_student).grid(row=2, column=0, columnspan=2)

# Labels and Entries for Assessments Tab
tk.Label(assessment_frame, text="Course ID").grid(row=0, column=0)
course_id_entry_assessment = tk.Entry(assessment_frame)
course_id_entry_assessment.grid(row=0, column=1)

tk.Label(assessment_frame, text="Assessment Name").grid(row=1, column=0)
assessment_name_entry = tk.Entry(assessment_frame)
assessment_name_entry.grid(row=1, column=1)

tk.Label(assessment_frame, text="Assessment Date (YYYY-MM-DD)").grid(row=2, column=0)
assessment_date_entry = tk.Entry(assessment_frame)
assessment_date_entry.grid(row=2, column=1)

tk.Label(assessment_frame, text="Total Marks").grid(row=3, column=0)
total_marks_entry = tk.Entry(assessment_frame)
total_marks_entry.grid(row=3, column=1)

tk.Button(assessment_frame, text="Create Assessment", command=create_assessment).grid(row=4, column=0, columnspan=2)

# Labels and Entries for Grades Tab
tk.Label(grade_frame, text="Assessment ID").grid(row=0, column=0)
assessment_id_entry = tk.Entry(grade_frame)
assessment_id_entry.grid(row=0, column=1)

tk.Label(grade_frame, text="Student ID").grid(row=1, column=0)
student_id_entry_grade = tk.Entry(grade_frame)
student_id_entry_grade.grid(row=1, column=1)

tk.Label(grade_frame, text="Obtained Marks").grid(row=2, column=0)
obtained_marks_entry = tk.Entry(grade_frame)
obtained_marks_entry.grid(row=2, column=1)

tk.Button(grade_frame, text="Record Grade", command=record_grade).grid(row=3, column=0, columnspan=2)

# Labels and Entries for View Grades Tab
tk.Label(view_grades_frame, text="Student ID").grid(row=0, column=0)
student_id_entry_view_grades = tk.Entry(view_grades_frame)
student_id_entry_view_grades.grid(row=0, column=1)

tk.Button(view_grades_frame, text="View Grades", command=view_grades).grid(row=1, column=0, columnspan=2)
show_deleted_button = tk.Button(root, text="Show Recently Deleted", command=show_recently_deleted)
show_deleted_button.grid(row=7, column=0, columnspan=6)
# Start the GUI event loop
root.mainloop()
