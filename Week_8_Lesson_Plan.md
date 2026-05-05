# Week 8: Conditional Logic & Data Transformation

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Implement conditional logic in SQL using CASE expressions.
- Handle NULL values safely with COALESCE and IFNULL.
- Perform basic data type conversions.

## 2. Concept Overview (Theory)
- **Why it matters**: Conditional logic allows analysts to create new, dynamic fields based on existing data, essential for segmenting customers or tagging transactions.
- **Example**: Categorizing orders as "High Value" if > $200 and "Standard" otherwise.

## 3. Guided Lab (MySQL Workbench)
- Use `CASE` to create a new column categorizing customer spending tiers.
- Use `COALESCE` to display 'No Email Provided' for NULL emails.

## 4. Independent Practice (Challenge)
1. Create a query that categorizes products by price: 'Low' (< $50), 'Medium' ($50-$200), 'High' (> $200).
2. Generate a report that replaces any missing country values with 'Unknown'.

## 5. Assessment & Validation
- Run the test script `tests/test_week8.py`.

## 6. Further Reading
- [MySQL CASE Expression](https://dev.mysql.com/doc/refman/8.0/en/control-flow-functions.html#operator_case)
