import pandas as pd

def detect_subscriptions(transactions):
    subscriptions = transactions[transactions['Description'].str.contains(
        'NETFLIX|SPOTIFY|AMAZON PRIME|HULU|APPLE MUSIC', case=False, na=False
    )]
    recurring = subscriptions.groupby('Description').filter(lambda x: len(x) > 1)
    return recurring

def suggest_savings(transactions):
    spending_categories = transactions.groupby('Category', as_index=False)['Amount'].sum()
    mean_spending = spending_categories['Amount'].mean()
    high_spending = spending_categories[spending_categories['Amount'] > mean_spending]
    
    print(f"Average spending per category: {mean_spending:.2f}\n")
    
    suggestions = []
    for _, row in high_spending.iterrows():
        suggestions.append(f"Consider reducing spending on {row['Category']}. You spent {row['Amount']:.2f}, which is above your average spend of {mean_spending:.2f}.")
    
    recurring_subs = detect_subscriptions(transactions)
    if not recurring_subs.empty:
        total_recurring = recurring_subs['Amount'].sum()
        suggestions.append(f"You have multiple subscriptions totaling {total_recurring:.2f}. Review and cancel those you no longer need.")
    
    return suggestions

# Sample Data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='W'),
    'Description': [
        'NETFLIX', 'GROCERIES', 'SPOTIFY', 'DINING', 'HULU', 'GAS', 'AMAZON PRIME', 'RENT',
        'APPLE MUSIC', 'SHOPPING', 'UBER', 'ELECTRIC BILL', 'WATER BILL', 'GYM MEMBERSHIP',
        'MOVIE THEATER', 'COFFEE', 'FAST FOOD', 'SUBSCRIPTION BOX', 'CAR PAYMENT',
        'INSURANCE', 'PHONE BILL', 'INTERNET BILL', 'PUBLIC TRANSPORT', 'BOOKSTORE',
        'CLOTHING', 'PHARMACY', 'AIRLINE TICKET', 'HOTEL', 'GAMING', 'CHARITY DONATION'
    ],
    'Category': [
        'Entertainment', 'Groceries', 'Entertainment', 'Dining', 'Entertainment', 'Transport', 'Entertainment', 'Housing',
        'Entertainment', 'Shopping', 'Transport', 'Utilities', 'Utilities', 'Health & Fitness',
        'Entertainment', 'Dining', 'Dining', 'Shopping', 'Transport',
        'Insurance', 'Utilities', 'Utilities', 'Transport', 'Shopping',
        'Shopping', 'Health', 'Travel', 'Travel', 'Entertainment', 'Charity'
    ],
    'Amount': [15.99, 120.50, 9.99, 45.00, 14.99, 30.00, 12.99, 1000.00, 9.99, 80.00, 
               25.50, 60.75, 40.25, 35.00, 50.00, 5.99, 12.49, 22.99, 400.00, 150.00,
               90.00, 85.00, 20.00, 30.00, 75.00, 45.00, 500.00, 600.00, 59.99, 100.00]
}


df = pd.DataFrame(data)

recommendations = suggest_savings(df)

for rec in recommendations:
    print(rec)
