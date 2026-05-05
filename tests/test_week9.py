from test_base import TestBase
import unittest

class TestWeek9Queries(TestBase):
    def test_ranking_function(self):
        # Validate Window Function Ranking
        query = """
        SELECT COUNT(*) FROM (
            SELECT employee_id, RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rnk
            FROM employees
        ) as ranked_emps;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 5, "Expected 5 ranked employees")

if __name__ == '__main__':
    unittest.main()
