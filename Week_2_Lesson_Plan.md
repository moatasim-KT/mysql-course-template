# Week 2: Refining Queries & Data Organization

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Filter data using complex operators (LIKE, IN, BETWEEN, IS NULL).
- Organize and sort query results effectively.
- Limit and control the volume of retrieved data.
- Handle and remove duplicate records.

## 2. Concept Overview (Theory)
- **Why it matters**: Real-world data is rarely clean or formatted exactly as needed. Mastering these refining techniques allows analysts to pinpoint relevant subsets of data quickly.
- **Example**: An analyst needs to find all customers in the US whose email addresses have not been verified (IS NULL).

## 3. Guided Lab (MySQL Workbench)
- Use `LIKE` with wildcards to search for email patterns.
- Use `BETWEEN` to filter orders by date range.
- Apply `ORDER BY` to find the highest total_amount orders.
- Practice `DISTINCT` to identify unique countries in the customer dataset.

## 4. Independent Practice (Challenge)
Using the `customers` and `orders` tables:
1. Find all customers whose name starts with 'A'.
2. List orders that occurred between 2023-02-01 and 2023-03-01.
3. Display a list of unique countries where our customers reside.

## 5. Assessment & Validation
- Run the test script `tests/test_week2.py` (to be created) to validate the query logic.

## 6. Further Reading
- [MySQL LIKE Operator](https://dev.mysql.com/doc/refman/8.0/en/string-comparison-functions.html)
- [MySQL ORDER BY](https://dev.mysql.com/doc/refman/8.0/en/select.html)
