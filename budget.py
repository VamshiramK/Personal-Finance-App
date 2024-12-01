from database import connect

def set_budget(user_id, category, limit):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO budgets (user_id, category, \"limit\") VALUES (?, ?, ?)", 
                       (user_id, category, limit))
        conn.commit()
        print(f"Budget set for {category} with a limit of {limit}.")

def update_budget(user_id, category, limit):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE budgets SET \"limit\" = ? WHERE user_id = ? AND category = ?", 
                       (limit, user_id, category))
        conn.commit()
        print(f"Budget for {category} updated to {limit}.")

def check_budget(user_id, category, amount):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT \"limit\" FROM budgets WHERE user_id = ? AND category = ?", 
                       (user_id, category))
        result = cursor.fetchone()
        if result:
            budget_limit = result[0]
            if amount > budget_limit:
                print(f"Warning: This expense exceeds your budget limit of {budget_limit} for {category}.")
        else:
            print(f"No budget set for {category}.")

