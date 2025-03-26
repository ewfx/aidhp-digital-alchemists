import pandas as pd
import unittest
from Banking_Ai_Savings import detect_subscriptions, suggest_savings

class TestBankingAISavings(unittest.TestCase):
    def setUp(self):
        self.test_data_positive = pd.DataFrame({
            'Description': ['NETFLIX', 'SPOTIFY', 'NETFLIX', 'DINING', 'RENT', 'GROCERIES', 'UBER', 'HULU', 'SHOPPING'],
            'Category': ['Entertainment', 'Entertainment', 'Entertainment', 'Dining', 'Housing', 'Groceries', 'Transport', 'Entertainment', 'Shopping'],
            'Amount': [15.99, 9.99, 15.99, 45.00, 1000.00, 120.50, 25.50, 14.99, 80.00]
        })
        
        self.test_data_negative = pd.DataFrame({
            'Description': ['GROCERIES', 'DINING', 'RENT', 'UBER', 'ELECTRIC BILL'],
            'Category': ['Groceries', 'Dining', 'Housing', 'Transport', 'Utilities'],
            'Amount': [50.00, 30.00, 800.00, 20.00, 60.00]
        })

    def test_detect_subscriptions_positive(self):
        result = detect_subscriptions(self.test_data_positive)
        self.assertGreater(len(result), 0, "Should detect at least one recurring subscription")

    def test_detect_subscriptions_negative(self):
        result = detect_subscriptions(self.test_data_negative)
        self.assertEqual(len(result), 0, "Should return an empty DataFrame when no subscriptions are present")

    def test_suggest_savings_positive(self):
        result = suggest_savings(self.test_data_positive)
        self.assertTrue(any("Consider reducing spending on Housing" in s for s in result), "Should suggest reducing high spending on Housing")
        self.assertTrue(any("You have multiple subscriptions" in s for s in result), "Should detect recurring subscriptions")

    def test_suggest_savings_negative(self):
        result = suggest_savings(self.test_data_negative)
        self.assertFalse(any("Consider reducing spending" in s for s in result), "Should not suggest savings when all spending is reasonable")

if __name__ == '__main__':
    unittest.main()
