# Week 3: Aggregation & Grouping

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Apply aggregate functions (COUNT, SUM, AVG, MIN, MAX) to derive insights.
- Group data using the GROUP BY clause.
- Filter aggregated results using the HAVING clause.
- Understand the order of execution for SQL queries involving aggregation.

## 2. Concept Overview (Theory)
- **Why it matters**: Data analysis is rarely about individual rows; it is about trends, sums, and averages. Aggregation allows analysts to summarize massive datasets into actionable business metrics.
- **Example**: Calculate total sales volume per customer to determine top spenders.

## 3. Guided Lab (MySQL Workbench)
- Use `SUM(total_amount)` to get total revenue.
- Use `GROUP BY customer_id` to break down revenue per customer.
- Use `HAVING` to filter for customers who spent more than $200 total.

## 4. Independent Practice (Challenge)
Using the `orders` table:
1. Find the total number of orders placed per customer.
2. Calculate the average order amount per country.
3. Identify customers who have placed more than 1 order.

## 5. Assessment & Validation
- Run the test script `tests/test_week3.py` to validate aggregation results.

## 6. Further Reading
- [MySQL Aggregate Functions](https://dev.mysql.com/doc/refman/8.0/en/group-by-functions.html)
- [Understanding HAVING vs WHERE](https://www.geeksforgeeks.org/sql-having-vs-where-clause/)
