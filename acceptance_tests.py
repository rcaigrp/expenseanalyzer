import pytest
import os

def test_criterion_1_module_import():
    try:
        import expense_analyzer
    except ImportError:
        pytest.fail("expense_analyzer module not found")

def test_criterion_2_analyze_expenses():
    from expense_analyzer import analyze_expenses
    expenses = [
        {"category": "Food", "amount": 100},
        {"category": "Food", "amount": 50},
        {"category": "Transport", "amount": 30}
    ]
    summary = analyze_expenses(expenses)
    assert "Food" in summary
    assert summary["Food"] == 150
    assert summary["Transport"] == 30

def test_criterion_3_generate_report():
    from expense_analyzer import generate_report
    summary = {"Food": 150, "Transport": 30}
    report_path = "/workspace/projects/ExpenseAnalyzer/report.txt"
    if os.path.exists(report_path):
        os.remove(report_path)
    generate_report(summary, report_path)
    assert os.path.exists(report_path)

def test_criterion_4_get_trending_categories():
    from expense_analyzer import get_trending_categories
    expenses = [
        {"category": "Food", "amount": 100},
        {"category": "Food", "amount": 50},
        {"category": "Transport", "amount": 30},
        {"category": "Entertainment", "amount": 10}
    ]
    top = get_trending_categories(expenses, top_n=3)
    assert top == ["Food", "Transport", "Entertainment"]
