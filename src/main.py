"""
main.py - Module principal pour l'application 'Installation Fenêtres'.

Ce module gère l'interface utilisateur.

Auteur: Alexis Boulet
Date: Août 2024
"""
from models.database import create_connection, create_tables
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
