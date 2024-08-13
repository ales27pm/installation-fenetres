import sqlite3
import os
from views.ui import create_main_window

DB_PATH = os.path.join(os.path.expanduser("~"), 'installation-fenetres', 'data', 'clients.db')

# Initialisation de la base de données
def init_db():
    print(f"Connecting to database at {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Création de la table clients
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

    # Création de la table soumissions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS soumissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            description TEXT,
            dimensions TEXT,
            couleur TEXT,
            prix REAL,
            date TEXT,
            FOREIGN KEY(client_id) REFERENCES clients(id)
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    create_main_window()

