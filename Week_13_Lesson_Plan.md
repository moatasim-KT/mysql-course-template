# Week 13: Database Design for Analysts

## 1. Learning Objectives
By the end of this lesson, students will be able to:
- Understand basic Database Normalization (1NF, 2NF, 3NF).
- Create Entity-Relationship (ER) diagrams to model business scenarios.
- Design efficient schemas for analytical reporting.

## 2. Concept Overview (Theory)
- **Why it matters**: Understanding how data is structured allows analysts to query it more effectively and identify potential data quality issues at the source.
- **Example**: Breaking down a flat, denormalized spreadsheet of orders into related `customers`, `orders`, and `products` tables to improve consistency.

## 3. Guided Lab (MySQL Workbench)
- Use the MySQL Workbench Model tool to reverse-engineer the current database schema into an ER diagram.
- Discuss how to split a hypothetical "flat" table into normalized tables.

## 4. Independent Practice (Challenge)
1. Sketch an ER diagram for a library system (Books, Authors, Loans).
2. Propose a normalized schema based on your sketch.

## 5. Assessment & Validation
- Submit your ER diagram and schema proposal.

## 6. Further Reading
- [Database Normalization Explained](https://www.geeksforgeeks.org/database-normalization-1nf-2nf-3nf/)
