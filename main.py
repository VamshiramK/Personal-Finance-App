from database import initialize_database, connect
from transaction import user_dashboard

def register_user(username, password):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully.")

def login_user(username, password):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        if result:
            print("Login successful.")
            return result[0]  # Return user_id
        else:
            print("Invalid credentials.")
            return None

def main_menu():
    initialize_database()
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = login_user(username, password)
            if user_id:
                user_dashboard(user_id)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
