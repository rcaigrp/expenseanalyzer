class ExpenseAnalyzer:
    def __init__(self, expenses):
        self.expenses = expenses

    def analyze_spending(self):
        spending = {}
        for exp in self.expenses:
            cat = exp.get('category')
            amt = exp.get('amount')
            if cat in spending:
                spending[cat] += amt
            else:
                spending[cat] = amt
        return spending

    def generate_report(self):
        spending = self.analyze_spending()
        lines = ["Expense Report:", ""]
        lines.append(f"{'Category':<20} {'Amount':>10}")
        lines.append("-" * 30)
        for cat, total in spending.items():
            lines.append(f"{cat:<20} ${total:>10.2f}")
        return "\n".join(lines)

    def filter_by_category(self, category):
        return [e for e in self.expenses if e.get('category') == category]
