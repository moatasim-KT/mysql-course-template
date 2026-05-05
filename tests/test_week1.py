from test_base import TestBase
import unittest

class TestWeek1Queries(TestBase):
    def test_exercise_2_sales_department(self):
        # Student query result validation logic
        query = "SELECT COUNT(*) FROM employees WHERE department = 'Sales';"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 2, "Expected 2 employees in Sales department")

if __name__ == '__main__':
    unittest.main()
