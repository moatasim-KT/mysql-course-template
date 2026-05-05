-- Failure Analysis Exercise: Week 11
-- This query is running extremely slowly on a large dataset.
-- Task: Use EXPLAIN to analyze the query, identify why it is slow, and fix it by adding an index.

-- SLOW QUERY:
SELECT c.name, o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE c.country = 'USA';
