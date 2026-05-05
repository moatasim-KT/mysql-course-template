# Week 11: Performance Optimization I

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Use the `EXPLAIN` statement to analyze query execution plans.
- Understand how indexes improve query performance.
- Identify and resolve full table scans.
- Perform failure analysis on slow-running queries.

## 2. Concept Overview (Theory)
- **Why it matters**: Efficient queries are critical for performance, especially with large datasets common in data analytics.
- **Example**: A report query taking 10 minutes to run is unusable; optimizing the query structure and indexing can reduce it to milliseconds.

## 3. Guided Lab (MySQL Workbench)
- Run `EXPLAIN` on a slow query before and after adding an index on a frequently filtered column (e.g., `department`).
- **Failure Analysis Task**: Analyze `exercises/failure_analysis/week11_slow_query.sql` to identify bottlenecks.

## 4. Independent Practice (Challenge)
1. Analyze a query on the `orders` table and suggest an appropriate index.
2. Identify a "full table scan" and rewrite/index to avoid it.

## 5. Assessment & Validation
- Run the test script `tests/test_week11.py` and verify execution time improvements.

## 6. Further Reading
- [MySQL EXPLAIN Output](https://dev.mysql.com/doc/refman/8.0/en/explain-output.html)
- [MySQL Optimization](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
