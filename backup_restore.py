import shutil
from datetime import datetime

def backup_data():
    backup_file = f"finance_app_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.db"
    shutil.copy('finance_app.db', backup_file)
    print(f"Backup created: {backup_file}")

def restore_data(backup_file):
    shutil.copy(backup_file, 'finance_app.db')
    print(f"Database restored from {backup_file}")
