import unittest
from analyzer import analyze_spending_trends, generate_report, get_top_categories

class TestExpenseAnalyzer(unittest.TestCase):
    def test_criterion_1_module_import(self):
        import analyzer
        self.assertTrue(True)

    def test_criterion_2_analyze_spending_trends(self):
        data = [
            {"date": "2023-01-01", "amount": 10.0, "category": "Food"},
            {"date": "2023-01-02", "amount": 20.0, "category": "Food"},
            {"date": "2023-02-01", "amount": 5.0, "category": "Travel"}
        ]
        result = analyze_spending_trends(data)
        self.assertEqual(result, {"2023-01": 30.0, "2023-02": 5.0})

    def test_criterion_3_generate_report(self):
        data = [
            {"date": "2023-01-01", "amount": 10.0, "category": "Food"},
            {"date": "2023-01-02", "amount": 20.0, "category": "Food"}
        ]
        result = generate_report(data)
        self.assertIn("Total Spent: $30.00", result)
        self.assertIn("Total Transactions: 2", result)

    def test_criterion_4_get_top_categories(self):
        data = [
            {"date": "2023-01-01", "amount": 100.0, "category": "Food"},
            {"date": "2023-01-02", "amount": 50.0, "category": "Travel"},
            {"date": "2023-01-03", "amount": 10.0, "category": "Food"}
        ]
        result = get_top_categories(data, n=1)
        self.assertEqual(result, ["Food"])

if __name__ == '__main__':
    unittest.main()
