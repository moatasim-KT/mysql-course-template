# Week 5: Complex Joins & Set Operations

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Combine data from more than two tables using multi-table JOINs.
- Understand and apply set operators: UNION, UNION ALL, INTERSECT (simulated).
- Troubleshoot Cartesian products.
- Optimize join performance by understanding execution order.

## 2. Concept Overview (Theory)
- **Why it matters**: Complex data requirements often span multiple entities (e.g., Customers -> Orders -> OrderItems -> Products). Efficient multi-table joins are essential for assembling these relationships.
- **Example**: Generating a comprehensive invoice report linking customers, their orders, and the specific products purchased.

## 3. Guided Lab (MySQL Workbench)
- Use a 4-table join: `customers` -> `orders` -> `order_items` -> `products`.
- Use `UNION` to combine results from two separate employee datasets (simulating data migration).

## 4. Independent Practice (Challenge)
Using the new `products` and `order_items` tables:
1. List all products sold, along with the total quantity sold for each.
2. Find products that have never been ordered (LEFT JOIN + IS NULL).

## 5. Assessment & Validation
- Run the test script `tests/test_week5.py`.

## 6. Further Reading
- [MySQL Set Operators](https://dev.mysql.com/doc/refman/8.0/en/union.html)
