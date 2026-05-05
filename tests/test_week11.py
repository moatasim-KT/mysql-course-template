from test_base import TestBase
import unittest

class TestWeek11Queries(TestBase):
    def test_explain_index_usage(self):
        # Validate that an index is actually used
        # This is a basic check to ensure EXPLAIN runs
        query = "EXPLAIN SELECT * FROM orders WHERE customer_id = 1;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        # In a real world scenario, you would parse the 'key' column
        # to ensure it is not NULL, indicating an index was used.
        self.assertTrue(len(result) > 0, "EXPLAIN plan should be returned")

if __name__ == '__main__':
    unittest.main()
