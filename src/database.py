import sqlite3
import os

DB_PATH = os.path.join(os.path.expanduser("~"), 'installation-fenetres', 'data', 'clients.db')

def connect_db():
    print(f"Connecting to database at {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    conn = connect_db()
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


# Fonctions de gestion des clients
def add_client(nom, entreprise, personne_ressource, adresse, telephone, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clients (nom, entreprise, personne_ressource, adresse, telephone, email)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nom, entreprise, personne_ressource, adresse, telephone, email))
    conn.commit()
    conn.close()

def get_clients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

def get_client_by_id(client_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE id=?", (client_id,))
    client = cursor.fetchone()
    conn.close()
    return client

def update_client(client_id, nom, entreprise, personne_ressource, adresse, telephone, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clients
        SET nom=?, entreprise=?, personne_ressource=?, adresse=?, telephone=?, email=?
        WHERE id=?
    ''', (nom, entreprise, personne_ressource, adresse, telephone, email, client_id))
    conn.commit()
    conn.close()

def delete_client(client_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
    conn.commit()
    conn.close()

# Fonctions de gestion des soumissions
def add_soumission(client_id, description, dimensions, couleur, prix, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO soumissions (client_id, description, dimensions, couleur, prix, date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (client_id, description, dimensions, couleur, prix, date))
    conn.commit()
    conn.close()

def get_soumissions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.id, c.nom, s.description, s.dimensions, s.couleur, s.prix, s.date
        FROM soumissions s
        JOIN clients c ON s.client_id = c.id
    ''')
    soumissions = cursor.fetchall()
    conn.close()
    return soumissions

def get_soumission_by_id(soumission_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM soumissions WHERE id=?", (soumission_id,))
    soumission = cursor.fetchone()
    conn.close()
    return soumission

def update_soumission(soumission_id, description, dimensions, couleur, prix, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE soumissions
        SET description=?, dimensions=?, couleur=?, prix=?, date=?
        WHERE id=?
    ''', (description, dimensions, couleur, prix, date, soumission_id))
    conn.commit()
    conn.close()

def delete_soumission(soumission_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soumissions WHERE id=?", (soumission_id,))
    conn.commit()
    conn.close()

