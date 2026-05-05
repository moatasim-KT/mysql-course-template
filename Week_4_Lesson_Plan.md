# Week 4: Joins & Relational Data

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Understand relational database design (Primary & Foreign Keys).
- Combine data from multiple tables using INNER JOIN.
- Handle unmatched rows using LEFT JOIN.
- Execute Self Joins for hierarchical data relationships.

## 2. Concept Overview (Theory)
- **Why it matters**: Data is normalized into multiple tables to reduce redundancy. Joins are the mechanism to reassemble this data for analysis.
- **Example**: Combining the `customers` and `orders` tables to view customer names alongside their order amounts.

## 3. Guided Lab (MySQL Workbench)
- Perform an `INNER JOIN` between `customers` and `orders` on `customer_id`.
- Observe how `LEFT JOIN` includes customers who haven't placed orders.

## 4. Independent Practice (Challenge)
Using `customers` and `orders`:
1. Generate a report showing customer names and their total spend across all orders.
2. Find customers who have NOT placed any orders (using LEFT JOIN and IS NULL).

## 5. Assessment & Validation
- Run the test script `tests/test_week4.py` to validate join results.

## 6. Further Reading
- [MySQL JOIN Syntax](https://dev.mysql.com/doc/refman/8.0/en/join.html)
- [Normalization vs Denormalization](https://www.geeksforgeeks.org/database-normalization-vs-denormalization/)
