import os

# Chemins des fichiers
home_dir = os.path.expanduser('~')
base_dir = os.path.join(home_dir, 'Cali', 'Installation_Fenetres', 'src')

# Créer les répertoires si nécessaire
os.makedirs(os.path.join(base_dir, 'models'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'views'), exist_ok=True)

# Contenu des fichiers
main_py = """from models.database import create_connection, create_tables
from views.ui import create_main_window

if __name__ == "__main__":
    # Créer la connexion à la base de données
    conn = create_connection()
    if conn is not None:
        # Créer les tables nécessaires
        create_tables(conn)
        conn.close()

    # Lancer l'interface utilisateur
    app = create_main_window()
    app.mainloop()
"""

database_py = """import sqlite3
import os

def create_connection():
    # Définir le chemin de la base de données
    home_dir = os.path.expanduser('~')
    db_path = os.path.join(home_dir, 'Cali', 'Installation_Fenetres', 'data', 'installation_fenetres.db')
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
        # Créer la table Clients
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
"""

ui_py = """import tkinter as tk

def create_main_window():
    root = tk.Tk()
    root.title("Installation Fenêtres")
    root.geometry("800x600")

    label = tk.Label(root, text="Bienvenue dans Installation Fenêtres", font=("Arial", 16))
    label.pack(pady=20)

    # Ajout de boutons pour gérer les clients, soumissions, etc.
    btn_clients = tk.Button(root, text="Gérer les clients", font=("Arial", 14))
    btn_clients.pack(pady=10)

    btn_soumissions = tk.Button(root, text="Gérer les soumissions", font=("Arial", 14))
    btn_soumissions.pack(pady=10)

    btn_installations = tk.Button(root, text="Gérer les installations", font=("Arial", 14))
    btn_installations.pack(pady=10)

    return root
"""

# Écrire les fichiers
with open(os.path.join(base_dir, 'main.py'), 'w') as file:
    file.write(main_py)

with open(os.path.join(base_dir, 'models', 'database.py'), 'w') as file:
    file.write(database_py)

with open(os.path.join(base_dir, 'views', 'ui.py'), 'w') as file:
    file.write(ui_py)

print("Fichiers créés avec succès!")
