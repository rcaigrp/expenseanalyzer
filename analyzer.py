def analyze_spending_trends(data):
    trends = {}
    for expense in data:
        date = expense.get('date', '')
        month = date[:7] if len(date) >= 7 else 'Unknown'
        amount = float(expense.get('amount', 0))
        trends[month] = trends.get(month, 0) + amount
    return trends

def generate_report(data):
    total = 0
    categories = {}
    for expense in data:
        amount = float(expense.get('amount', 0))
        category = expense.get('category', 'Other')
        total += amount
        categories[category] = categories.get(category, 0) + 1
    
    report = f"Total Spent: ${total:.2f}\n"
    report += f"Total Transactions: {len(data)}\n"
    report += "Breakdown:\n"
    for cat, count in sorted(categories.items()):
        report += f"  {cat}: {count} expenses\n"
    return report

def get_top_categories(data, n=5):
    categories = {}
    for expense in data:
        category = expense.get('category', 'Other')
        amount = float(expense.get('amount', 0))
        categories[category] = categories.get(category, 0) + amount
    
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    return [cat for cat, amount in sorted_categories[:n]]
