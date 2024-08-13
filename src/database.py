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
