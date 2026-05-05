# Teacher's Guide: MySQL for Data Analytics

## 1. Course Facilitation Philosophy
This course is built on the philosophy of **Active Engagement**. Instructors are facilitators, not lecturers. Your goal is to guide students to discover solutions themselves.

### Facilitation Techniques:
- **Socratic Questioning**: When a student asks "Why isn't this query working?", ask them "What does the `EXPLAIN` output tell you about how MySQL is reading these tables?" instead of giving the answer.
- **Peer Reviewing**: Encourage students to swap their `exercises/*.sql` files. They should look for:
    - Readability (CTEs vs subqueries).
    - Performance considerations.
    - Potential edge-case bugs (e.g., handling NULLs).
- **Error Analysis**: When a student gets a test failure, do not debug their code. Instead, help them write a test case to isolate the issue.

## 2. Common Pitfalls
- **Performance**: Students often forget to index foreign keys or frequently filtered columns. 
- **Join Logic**: Students frequently confuse INNER JOIN and LEFT JOIN, especially when dealing with NULL values.
- **Aggregation**: Students often forget to include non-aggregated columns in the GROUP BY clause.

## 3. Grading Rubric (for Capstone)
| Criteria | Excellent (5) | Satisfactory (3) | Needs Improvement (1) |
| :--- | :--- | :--- | :--- |
| **Schema Design** | Normalized, performant, documented. | Functionally correct but unoptimized. | Fails to support queries effectively. |
| **Query Logic** | Efficient, readable (uses CTEs), correct. | Correct but complex/messy. | Inefficient or incorrect results. |
| **Data Quality** | Proactive data cleaning/handling. | Basic cleaning. | Ignores data inconsistencies. |
| **Documentation** | Clear, professional. | Sufficient. | Lacks clear explanation. |
