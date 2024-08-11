import sqlite3
import os

def create_connection():
    # Utilise un chemin absolu basé sur le répertoire de l'utilisateur
    home_dir = os.path.expanduser('~')
    db_path = os.path.join(home_dir, 'installation-fenetres', 'data', 'installation_fenetres.db')
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print("Connexion à la base de données réussie!")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_client TEXT NOT NULL,
                entreprise TEXT,
                personne_ressource TEXT,
                adresse TEXT,
                telephone TEXT,
                email TEXT
            )
        ''')
        conn.commit()
        print("Tables créées avec succès!")
    except sqlite3.Error as e:
        print(e)

