# EduSchema Management System

EduSchema Management System is a comprehensive application designed to manage courses, instructors, enrollments, assessments, and grades for an educational institution. The system is built using Python's Tkinter for the GUI and MySQL for the backend database. This project provides a user-friendly interface to perform CRUD operations and manage the various entities within the educational domain.

Features

Course Management: Add, update, and remove courses.
Instructor Management: Add, update, and delete instructors.
Student Enrollment: Enroll students in courses.
Assessment Management: Create assessments for courses.
Grade Management: Record and view student grades.
Deleted Records Log: View recently deleted records for auditing purposes.
Prerequisites

Python 3.x
Tkinter
MySQL server
MySQL Connector for Python


Application Setup

Install MySQL Connector:
pip install mysql-connector-python
Run the Application:
Save the provided Python code into a file, for example, eduschema.py, and run it:


python eduschema.py
Functionality

Course Management
Add Course: Enter the course details and click on "Add Course".
Update Course: Modify the course details and click on "Update Course".
Remove Course: Enter the course ID and click on "Remove Course" to deactivate the course.
Instructor Management
Add Instructor: Enter the instructor details and click on "Add Instructor".
Update Instructor: Modify the instructor details and click on "Update Instructor".
Delete Instructor: Enter the instructor ID and click on "Delete Instructor" to deactivate the instructor.
Student Enrollment
Enroll Student: Enter the student ID and course ID, then click on "Enroll Student".
Assessment Management
Create Assessment: Enter the assessment details and click on "Create Assessment".
Grade Management
Record Grade: Enter the assessment ID, student ID, and obtained marks, then click on "Record Grade".
View Grades
View Grades: Enter the student ID and click on "View Grades" to see all grades for the student.
Deleted Records Log
Show Recently Deleted: Click on "Show Recently Deleted" to view the recently deleted records.
Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any features, bug fixes, or enhancements.

License

This project is licensed under the MIT License. See the LICENSE file for details.
