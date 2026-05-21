class ExpenseAnalyzer:
    def __init__(self, expenses=None):
        self.expenses = expenses or []

    def analyze_spending(self):
        totals = {}
        for exp in self.expenses:
            cat = exp.get('category')
            amt = exp.get('amount', 0)
            totals[cat] = totals.get(cat, 0) + amt
        return totals

    def generate_report(self):
        totals = self.analyze_spending()
        if not totals:
            return "No expenses recorded."
        lines = ["Expense Report:"]
        for cat, total in totals.items():
            lines.append(f"  {cat}: ${total:.2f}")
        return "\n".join(lines)

    def filter_by_category(self, category):
        return [e for e in self.expenses if e.get('category') == category]
