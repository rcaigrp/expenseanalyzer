import unittest
from analyzer import ExpenseAnalyzer

class TestExpenseAnalyzer(unittest.TestCase):
    def test_criterion_1_module_import(self):
        self.assertTrue(True)

    def test_criterion_2_analyze_spending(self):
        expenses = [
            {'category': 'Food', 'amount': 10.0},
            {'category': 'Food', 'amount': 20.0},
            {'category': 'Transport', 'amount': 5.0}
        ]
        analyzer = ExpenseAnalyzer(expenses)
        spending = analyzer.analyze_spending()
        self.assertEqual(spending['Food'], 30.0)
        self.assertEqual(spending['Transport'], 5.0)

    def test_criterion_3_generate_report(self):
        expenses = [
            {'category': 'Food', 'amount': 10.0}
        ]
        analyzer = ExpenseAnalyzer(expenses)
        report = analyzer.generate_report()
        self.assertIn('Food', report)
        self.assertIn('10.00', report)

    def test_criterion_4_filter_by_category(self):
        expenses = [
            {'category': 'Food', 'amount': 10.0},
            {'category': 'Transport', 'amount': 5.0}
        ]
        analyzer = ExpenseAnalyzer(expenses)
        result = analyzer.filter_by_category('Food')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], 10.0)
