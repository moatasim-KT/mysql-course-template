from test_base import TestBase
import unittest

class TestWeek4Queries(TestBase):
    def test_join_customers_orders(self):
        # Validate that the join between customers and orders works
        query = "SELECT COUNT(*) FROM customers c JOIN orders o ON c.customer_id = o.customer_id;"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 7, "Expected 7 orders joined with customers")

if __name__ == '__main__':
    unittest.main()
