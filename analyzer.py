expenses = []

def add_expense(expense):
    expenses.append(expense)

def analyze_spending():
    totals = {}
    for exp in expenses:
        cat = exp.get('category')
        amt = float(exp.get('amount', 0))
        totals[cat] = totals.get(cat, 0) + amt
    return totals

def generate_report():
    totals = analyze_spending()
    if not totals:
        return "No expenses recorded."
    lines = ["Expense Report:"]
    for cat, total in sorted(totals.items()):
        lines.append(f"- {cat}: ${total:.2f}")
    return "\n".join(lines)

def filter_by_category(category):
    return [e for e in expenses if e.get('category') == category]
