CREATE DATABASE eduschema;
use eduschema;

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    course_description TEXT,
    course_duration INT,
    course_category VARCHAR(50),
    course_level VARCHAR(20),
    course_status VARCHAR(10) DEFAULT 'Active'
);

CREATE TABLE Instructors (
    instructor_id INT PRIMARY KEY,
    instructor_name VARCHAR(100) NOT NULL,
    instructor_email VARCHAR(100),
    instructor_bio TEXT,
    specialization_area VARCHAR(50)
);

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_email VARCHAR(100),
    student_date_of_birth DATE,
    student_enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completion_status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Assessments (
    assessment_id INT PRIMARY KEY,
    course_id INT,
    assessment_name VARCHAR(100),
    assessment_date DATE,
    total_marks INT,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Grades (
    grade_id INT PRIMARY KEY,
    assessment_id INT,
    student_id INT,
    obtained_marks INT,
    FOREIGN KEY (assessment_id) REFERENCES Assessments(assessment_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

CREATE TABLE recently_deleted (
    id INT AUTO_INCREMENT PRIMARY KEY,
    deleted_table VARCHAR(50) NOT NULL,
    deleted_record_id INT NOT NULL
);
DELETE FROM recently_deleted WHERE id = 8;


SELECT * FROM Courses;