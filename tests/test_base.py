import mysql.connector
import unittest
import os

# Base test class to handle DB connection for all weekly tests
class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "password"),
            database=os.environ.get("DB_NAME", "employees_db")
        )
        cls.cursor = cls.conn.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()
