# Week 7: String & Date Functions

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Manipulate text data using string functions (CONCAT, SUBSTRING, REPLACE).
- Perform date and time arithmetic (DATEDIFF, DATE_ADD).
- Format date/time fields for reporting.

## 2. Concept Overview (Theory)
- **Why it matters**: Data often comes in messy formats. String and date functions are critical for cleaning and preparing this data for analysis.
- **Example**: Combining first and last names into a single column, or calculating the time between an order date and a shipping date.

## 3. Guided Lab (MySQL Workbench)
- Use `CONCAT` to merge first and last names.
- Use `DATEDIFF` to calculate order processing time.

## 4. Independent Practice (Challenge)
1. Create a formatted string "Name (Country)" for each customer.
2. Identify all orders placed in the last month.

## 5. Assessment & Validation
- Run the test script `tests/test_week7.py`.

## 6. Further Reading
- [MySQL String Functions](https://dev.mysql.com/doc/refman/8.0/en/string-functions.html)
- [MySQL Date Functions](https://dev.mysql.com/doc/refman/8.0/en/date-and-time-functions.html)
