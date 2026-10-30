def analyze_budget(budget, fee_percent, exchange_rates, expenses):
    total_spent = 0.0
    category_spending = {}

    for amount, currency, category in expenses:
        rate = exchange_rates.get(currency, 1.0)
        converted = amount * rate
        fee = converted * (fee_percent / 100.0)
        final_cost = converted + fee
        
        total_spent += final_cost
        category_spending[category] = category_spending.get(category, 0.0) + final_cost

    remaining = budget - total_spent
    largest_category = max(category_spending, key=category_spending.get)
    largest_amount = category_spending[largest_category]

    print(f"Total Budget: {budget:.2f}")
    print(f"Total Spent: {total_spent:.2f}")
    if remaining >= 0:
        print(f"Remaining Budget: {remaining:.2f}")
    else:
        print(f"Budget Exceeded By: {abs(remaining):.2f}")
    print(f"Largest Category: {largest_category} ({largest_amount:.2f})")


budget = 2500.00
fee_percentage = 2.0
rates = {
    "USD": 1.0,
    "EUR": 1.08,
    "JPY": 0.0067,
    "GBP": 1.27
}
expenses = [
    (120.0, "EUR", "Lodging"),
    (45.0, "GBP", "Food"),
    (15000.0, "JPY", "Transport"),
    (300.0, "EUR", "Lodging"),
    (80.0, "USD", "Activities")
]

analyze_budget(budget, fee_percentage, rates, expenses)
