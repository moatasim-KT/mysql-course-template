# Week 12: Performance Optimization II & Views

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Create and utilize Views to abstract complex queries and enhance security.
- Introduce Stored Procedures for automating repetitive tasks.
- Understand basic transaction management.

## 2. Concept Overview (Theory)
- **Why it matters**: Views allow analysts to present a simplified interface to complex underlying schemas. Stored procedures help standardize data manipulation across the team.
- **Example**: Creating a `sales_summary_view` so other analysts don't need to write the complex multi-table join every time they want a report.

## 3. Guided Lab (MySQL Workbench)
- Create a `View` that joins `customers`, `orders`, and `order_items`.
- Write a basic `Stored Procedure` to generate a report for a specific department.

## 4. Independent Practice (Challenge)
1. Create a `View` that calculates total spend per customer.
2. Create a `Stored Procedure` that takes a `category` as input and returns all products in that category.

## 5. Assessment & Validation
- Run the test script `tests/test_week12.py`.

## 6. Further Reading
- [MySQL CREATE VIEW](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)
- [MySQL Stored Procedures](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
