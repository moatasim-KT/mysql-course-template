# Week 1: Introduction to MySQL for Data Analytics

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Establish a connection to a MySQL Server using MySQL Workbench.
- Understand the basic database architecture and table structures.
- Execute fundamental SELECT queries to retrieve and explore data.
- Filter and refine data results using the WHERE clause.

## 2. Concept Overview (Theory)
- **What is MySQL?**: A widely used relational database management system (RDBMS) that stores data in structured tables.
- **Why it matters for Data Analytics**: SQL is the universal language of data. Being able to efficiently query and extract data from databases is a core skill for any analyst.
- **Example**: An e-commerce analyst uses SQL to filter customer databases to identify high-value segments for targeted marketing campaigns.

## 3. Guided Lab (MySQL Workbench)
1. **Connect**: Open MySQL Workbench and establish a connection to your local MySQL instance.
2. **Schema Setup**: Run the provided `schema.sql` to initialize the `employees_db` database.
3. **Data Import**: Use the MySQL Workbench Import Wizard to load `data/employees.csv` into the `employees` table.
4. **Data Exploration**: 
   - Execute: `SELECT * FROM employees;` to view all data.
   - Execute: `SELECT first_name, salary FROM employees;` to select specific columns.

## 4. Independent Practice (Challenge)
Using the imported `employees` table, answer the following business question:
*Problem: Identify all employees who work in the 'Sales' department.*

- Open `exercises/week1.sql` and add your query to address the problem.

## 5. Assessment & Validation
- Run the provided test script `tests/test_week1.py` to validate your solution.
- The script checks if your query correctly identifies the expected number of employees in the Sales department.
- A successful validation means the test script runs without errors.

## 6. Further Reading
- [MySQL 8.0 Reference Manual: SELECT Statement](https://dev.mysql.com/doc/refman/8.0/en/select.html)
- [Introduction to Relational Databases](https://www.geeksforgeeks.org/introduction-of-rdbms/)
