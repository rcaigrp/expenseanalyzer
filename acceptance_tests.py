import pytest
import analyzer

@pytest.fixture
def reset_expenses():
    analyzer.expenses.clear()
    yield
    analyzer.expenses.clear()

def test_criterion_1_module_import():
    assert hasattr(analyzer, 'analyze_spending')
    assert hasattr(analyzer, 'generate_report')
    assert hasattr(analyzer, 'filter_by_category')

def test_criterion_2_analyze_spending_trends(reset_expenses):
    analyzer.add_expense({'category': 'Food', 'amount': 10.0})
    analyzer.add_expense({'category': 'Food', 'amount': 5.0})
    analyzer.add_expense({'category': 'Travel', 'amount': 100.0})
    totals = analyzer.analyze_spending()
    assert totals == {'Food': 15.0, 'Travel': 100.0}

def test_criterion_3_generate_report(reset_expenses):
    analyzer.add_expense({'category': 'Food', 'amount': 10.0})
    report = analyzer.generate_report()
    assert isinstance(report, str)
    assert "Food" in report
    assert "$10.00" in report

def test_criterion_4_filter_by_category(reset_expenses):
    analyzer.add_expense({'category': 'Food', 'amount': 10.0})
    analyzer.add_expense({'category': 'Travel', 'amount': 50.0})
    filtered = analyzer.filter_by_category('Food')
    assert len(filtered) == 1
    assert filtered[0]['category'] == 'Food'
