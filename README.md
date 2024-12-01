Features
User Registration and Authentication:

Register with a unique username and password.
Login functionality for existing users.
Income and Expense Tracking:

Add, update, delete income and expense entries.
Categorize transactions (e.g., Food, Rent, Salary).
Budget Management:

Set and update monthly budgets for specific categories.
Notify users when they exceed their budgets.
Financial Reports:

Generate monthly and yearly reports.
Calculate total income, expenses, and savings.
Data Persistence:

All data is stored in an SQLite database (finance_app.db).
Automatic table creation for users, transactions, and budgets.
Error Handling:

Graceful handling of invalid inputs and database errors.
Installation
Follow these steps to set up and run the application:

Prerequisites
Python:

Ensure Python 3.8 or later is installed.
You can download it from python.org.
SQLite:

SQLite is bundled with Python, so no separate installation is required.
Text Editor:

Use Visual Studio Code or any other editor.
Project Setup
Clone or download the project to your local machine:

bash
Copy code
git clone https://github.com/your-repo/personal-finance-manager.git
cd personal-finance-manager
Create a new directory and add the following structure:

arduino
Copy code
PersonalFinanceApp/
├── database.py
├── main.py
├── user.py
├── transaction.py
├── budget.py
├── finance_app.db (auto-created)
└── README.md
Install dependencies (if any). No additional libraries are required beyond standard Python.

Initialize the database:

bash
Copy code
python -c "from database import initialize_db; initialize_db()"
You should see:

csharp
Copy code
Database initialized with required tables.
