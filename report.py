from database import connect
from datetime import datetime

def generate_report(user_id, period='monthly'):
    with connect() as conn:
        cursor = conn.cursor()

        if period == 'monthly':
            month = datetime.now().strftime('%Y-%m')
            cursor.execute("SELECT type, SUM(amount) FROM transactions WHERE user_id = ? AND date LIKE ? GROUP BY type", (user_id, f"{month}%"))
        elif period == 'yearly':
            year = datetime.now().strftime('%Y')
            cursor.execute("SELECT type, SUM(amount) FROM transactions WHERE user_id = ? AND date LIKE ? GROUP BY type", (user_id, f"{year}%"))

        transactions = cursor.fetchall()
        total_income = sum(amount for type, amount in transactions if type == 'income')
        total_expenses = sum(amount for type, amount in transactions if type == 'expense')
        savings = total_income - total_expenses

        print(f"\n{period.capitalize()} Report:")
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Savings: {savings}")
