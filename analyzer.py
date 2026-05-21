def analyze_spending(expenses):
    totals = {}
    for exp in expenses:
        cat = exp['category']
        totals[cat] = totals.get(cat, 0) + exp['amount']
    return totals

def generate_report(totals):
    lines = ["Expense Report:"]
    for cat, total in sorted(totals.items()):
        lines.append(f"- {cat}: ${total:.2f}")
    return "\n".join(lines)

def filter_by_category(expenses, category):
    return [exp for exp in expenses if exp['category'] == category]
