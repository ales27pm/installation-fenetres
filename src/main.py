import sqlite3
import os
from views.ui import create_main_window

# Initialisation de la base de données
def init_db():
    db_path = os.path.join('/home/kali/installation-fenetres/data', 'clients.db')
    print(f"Connecting to database at {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        entreprise TEXT,
        personne_ressource TEXT,
        adresse TEXT,
        telephone TEXT,
        email TEXT
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    create_main_window()
