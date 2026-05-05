# Week 10: Advanced Data Cleaning

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Identify malformed data and outliers using SQL queries.
- Clean and standardize data using update operations and conditional logic.
- Handle missing values (NULLs) via imputation or exclusion.

## 2. Concept Overview (Theory)
- **Why it matters**: "Garbage in, garbage out." Analytics results are only as good as the underlying data. Analysts spend the majority of their time cleaning data.
- **Example**: Standardizing mismatched email formats or correcting case-sensitivity in categorical fields.

## 3. Guided Lab (MySQL Workbench)
- Find records with unrealistic salary values (outliers).
- Standardize customer email formats to lowercase.

## 4. Independent Practice (Challenge)
1. Write a query to detect duplicate `employee_id` entries (if any exist due to ingestion errors).
2. Clean up a table where `department` names are mixed-case (e.g., 'sales', 'Sales', 'SALES').

## 5. Assessment & Validation
- Run the test script `tests/test_week10.py`.

## 6. Further Reading
- [Data Cleaning Techniques](https://www.dataquest.io/blog/data-cleaning-techniques/)
