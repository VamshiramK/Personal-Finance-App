# test_personal_finance_app.py
import unittest
from user import register_user, login_user
from transaction import add_transaction, delete_transaction
from database import connect

class TestPersonalFinanceApp(unittest.TestCase):
    
    def test_register_user(self):
        self.assertIsNone(register_user("testuser", "password123"))
    
    def test_login_user(self):
        user_id = login_user("testuser", "password123")
        self.assertIsNotNone(user_id)
    
    def test_add_delete_transaction(self):
        user_id = login_user("testuser", "password123")
        add_transaction(user_id, 'expense', 'Food', 50, '2024-11-13')
        
        with connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
            transactions = cursor.fetchall()
            self.assertTrue(len(transactions) > 0)
            
            transaction_id = transactions[0][0]
            delete_transaction(transaction_id)
            cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
            self.assertIsNone(cursor.fetchone())

if __name__ == '__main__':
    unittest.main()
