from test_base import TestBase
import unittest

class TestWeek5Queries(TestBase):
    def test_four_table_join(self):
        # Validate multi-table join
        query = """
        SELECT COUNT(*) 
        FROM customers c 
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN products p ON oi.product_id = p.product_id;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]
        # Based on the sample data created earlier:
        self.assertEqual(result, 9, "Expected 9 total items sold across all orders")

if __name__ == '__main__':
    unittest.main()
