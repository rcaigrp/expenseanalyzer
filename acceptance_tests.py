import pytest
import sys
sys.path.insert(0, '/workspace/projects/ExpenseAnalyzer')
import analyzer

def test_criterion_1_module_import():
    import analyzer
    assert analyzer is not None

def test_criterion_2_analyze_spending():
    expenses = [
        {'category': 'Food', 'amount': 10.0},
        {'category': 'Food', 'amount': 5.0},
        {'category': 'Transport', 'amount': 15.0}
    ]
    result = analyzer.analyze_spending(expenses)
    assert result == {'Food': 15.0, 'Transport': 15.0}

def test_criterion_3_generate_report():
    totals = {'Food': 15.0, 'Transport': 15.0}
    report = analyzer.generate_report(totals)
    assert "Expense Report:" in report
    assert "Food" in report
    assert "Transport" in report

def test_criterion_4_filter_by_category():
    expenses = [
        {'category': 'Food', 'amount': 10.0},
        {'category': 'Transport', 'amount': 15.0},
        {'category': 'Food', 'amount': 5.0}
    ]
    result = analyzer.filter_by_category(expenses, 'Food')
    assert len(result) == 2
    assert all(exp['category'] == 'Food' for exp in result)
