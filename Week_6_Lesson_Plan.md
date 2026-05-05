# Week 6: Subqueries & CTEs

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Write nested subqueries to solve complex data filtering needs.
- Utilize Common Table Expressions (CTEs) to simplify query structure and improve readability.
- Understand the difference between correlated and non-correlated subqueries.

## 2. Concept Overview (Theory)
- **Why it matters**: Sometimes you need to perform an operation on a subset of data before running the main query. Subqueries and CTEs provide a way to build these temporary, logical datasets within a single query.
- **Example**: Find all customers whose total spending is greater than the average total spending across all customers.

## 3. Guided Lab (MySQL Workbench)
- Use a subquery to calculate the average order amount in the WHERE clause.
- Refactor the same query using a CTE (WITH clause).

## 4. Independent Practice (Challenge)
1. Using a CTE, identify the top-performing product category by total sales quantity.
2. Use a subquery to find all orders that are higher than the overall average order amount.

## 5. Assessment & Validation
- Run the test script `tests/test_week6.py`.

## 6. Further Reading
- [MySQL Subqueries](https://dev.mysql.com/doc/refman/8.0/en/subqueries.html)
- [MySQL CTEs](https://dev.mysql.com/doc/refman/8.0/en/with.html)
