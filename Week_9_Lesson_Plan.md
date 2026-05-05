# Week 9: Window Functions

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Use window functions (OVER, PARTITION BY, ORDER BY) to perform complex calculations without collapsing rows.
- Implement ranking functions (ROW_NUMBER, RANK, DENSE_RANK).
- Utilize value functions (LAG, LEAD) to compare row values.

## 2. Concept Overview (Theory)
- **Why it matters**: Aggregation functions collapse rows; window functions allow you to perform calculations across a set of rows while keeping individual row details. This is crucial for trend analysis and comparative reporting.
- **Example**: Comparing an employee's salary to the department average without hiding individual salary data.

## 3. Guided Lab (MySQL Workbench)
- Use `PARTITION BY` with `SUM()` to calculate running totals of sales per employee.
- Use `RANK()` to rank employees by salary within their department.

## 4. Independent Practice (Challenge)
Using the `performance_reviews` and `employees` tables:
1. Rank employees by their latest `performance_score` within their department.
2. Calculate the difference in `performance_score` between consecutive reviews for the same employee.

## 5. Assessment & Validation
- Run the test script `tests/test_week9.py`.

## 6. Further Reading
- [MySQL Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html)
