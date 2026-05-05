-- Schema update: Adding Performance Reviews for Advanced Analytics
USE employees_db;

CREATE TABLE performance_reviews (
    review_id INT PRIMARY KEY,
    employee_id INT,
    review_date DATE,
    performance_score INT,
    review_comments TEXT,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
