import pytest
from analyzer import ExpenseAnalyzer

@pytest.fixture
def analyzer():
    expenses = [
        {"category": "Food", "amount": 20.0},
        {"category": "Food", "amount": 15.0},
        {"category": "Transport", "amount": 10.0}
    ]
    return ExpenseAnalyzer(expenses)

def test_criterion_1_module_import():
    try:
        from analyzer import ExpenseAnalyzer
        assert True
    except ImportError:
        assert False

def test_criterion_2_analyze_spending(analyzer):
    result = analyzer.analyze_spending()
    assert result == {"Food": 35.0, "Transport": 10.0}

def test_criterion_3_generate_report(analyzer):
    result = analyzer.generate_report()
    assert isinstance(result, str)
    assert "Food" in result
    assert "Transport" in result

def test_criterion_4_filter_by_category(analyzer):
    result = analyzer.filter_by_category("Food")
    assert len(result) == 2
    assert all(e["category"] == "Food" for e in result)
