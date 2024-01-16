import unittest
import pyodbc
import pandas as pd
import datetime

# Importing the py file containing the functions to be tested
from Client_Info_Gathering import generate_client_id, insert_client

class TestClientInfoFunctionality(unittest.TestCase):

    def setUp(self):
        # Connection String
        self.conn_string = (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=AnkushBL\SQLEXPRESS;"
            "Database=Inventory;"
            "Trusted_Connection=yes;")
        self.test_conn = pyodbc.connect(self.conn_string)
        self.test_cursor = self.test_conn.cursor()

    def tearDown(self):
        # Close the test database connection after each test
        self.test_cursor.close()
        self.test_conn.close()

    def test_generate_client_id(self):            # Testing generate client id function
        # Insert a dummy record (The name should be in the table before)
        self.test_cursor.execute("INSERT INTO Client_Info (ClientID, Name) VALUES (?, ?)", ("2301ABC01", "Ankush"))
        self.test_conn.commit()

        generated_id = generate_client_id("Ankush")

        # Generated ID must be different from the inserted one!!
        self.assertNotEqual(generated_id, "2301ABC01")

    def test_insert_client(self):         # Testing the insert_client function
        # Gather client information for testing
        test_name = "TestClient"
        test_phone_num = "1234567890"
        test_gender = "M"
        test_age = 25
        test_op_procedure = "Test Procedure"
        test_amount = 100.0

        # Inserting Data
        insert_client(test_name, test_phone_num, test_gender, test_age, test_op_procedure, test_amount)

        # Fetching inserted data from database
        self.test_cursor.execute("SELECT * FROM Client_Info WHERE Name = ?", (test_name,))
        inserted_data = self.test_cursor.fetchone()

        # Checking if it matches
        self.assertIsNotNone(inserted_data)
        self.assertEqual(inserted_data.Name, test_name)
        self.assertEqual(inserted_data.PhoneNum, test_phone_num)
        self.assertEqual(inserted_data.Gender, test_gender)
        self.assertEqual(inserted_data.Age, test_age)
        self.assertEqual(inserted_data.OPProcedure, test_op_procedure)
        self.assertEqual(inserted_data.Amount, test_amount)

if __name__ == '__main__':
    unittest.main()