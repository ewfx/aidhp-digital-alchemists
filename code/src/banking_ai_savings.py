import pandas as pd
import numpy as np

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

# Generate a large sample dataset
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=200, freq='D')
descriptions = [
    'NETFLIX', 'GROCERIES', 'SPOTIFY', 'DINING', 'HULU', 'GAS', 'AMAZON PRIME', 'RENT',
    'APPLE MUSIC', 'SHOPPING', 'UBER', 'ELECTRIC BILL', 'WATER BILL', 'GYM MEMBERSHIP',
    'MOVIE THEATER', 'COFFEE', 'FAST FOOD', 'SUBSCRIPTION BOX', 'CAR PAYMENT',
    'INSURANCE', 'PHONE BILL', 'INTERNET BILL', 'PUBLIC TRANSPORT', 'BOOKSTORE',
    'CLOTHING', 'PHARMACY', 'AIRLINE TICKET', 'HOTEL', 'GAMING', 'CHARITY DONATION',
    'RESTAURANT', 'TAXI', 'MEDICAL BILL', 'EDUCATION', 'PARKING', 'HOME MAINTENANCE',
    'FURNITURE', 'ELECTRONICS', 'GIFT', 'PET CARE'
]
categories = [
    'Entertainment', 'Groceries', 'Entertainment', 'Dining', 'Entertainment', 'Transport', 'Entertainment', 'Housing',
    'Entertainment', 'Shopping', 'Transport', 'Utilities', 'Utilities', 'Health & Fitness',
    'Entertainment', 'Dining', 'Dining', 'Shopping', 'Transport',
    'Insurance', 'Utilities', 'Utilities', 'Transport', 'Shopping',
    'Shopping', 'Health', 'Travel', 'Travel', 'Entertainment', 'Charity',
    'Dining', 'Transport', 'Health', 'Education', 'Transport', 'Home',
    'Home', 'Electronics', 'Gifts', 'Pets'
]
amounts = np.random.uniform(5, 2000, size=500).round(2)

large_data = pd.DataFrame({
    'Date': np.random.choice(dates, size=500, replace=True),
    'Description': np.random.choice(descriptions, size=500, replace=True),
    'Category': np.random.choice(categories, size=500, replace=True),
    'Amount': amounts
})

recommendations = suggest_savings(large_data)

for rec in recommendations:
    print(rec)
