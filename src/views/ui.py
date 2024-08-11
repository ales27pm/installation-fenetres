import tkinter as tk
from tkinter import messagebox
from models.database import create_connection

def create_main_window():
    root = tk.Tk()
    root.title("Installation Fenêtres")
    root.geometry("800x600")

    label = tk.Label(root, text="Bienvenue dans Installation Fenêtres", font=("Arial", 16))
    label.pack(pady=20)

    # Bouton pour créer un client
    btn_create_client = tk.Button(root, text="Créer un client", font=("Arial", 14), command=create_client)
    btn_create_client.pack(pady=10)

    # Bouton pour afficher les clients
    btn_view_clients = tk.Button(root, text="Afficher les clients", font=("Arial", 14), command=view_clients)
    btn_view_clients.pack(pady=10)

    # Bouton pour modifier un client (fonctionnalité à ajouter)
    btn_edit_client = tk.Button(root, text="Modifier un client", font=("Arial", 14), command=edit_client)
    btn_edit_client.pack(pady=10)

    # Bouton pour supprimer un client (fonctionnalité à ajouter)
    btn_delete_client = tk.Button(root, text="Supprimer un client", font=("Arial", 14), command=delete_client)
    btn_delete_client.pack(pady=10)

    return root

# Fonction pour créer un client
def create_client():
    # Fenêtre pour ajouter un nouveau client
    client_window = tk.Toplevel()
    client_window.title("Créer un nouveau client")

    tk.Label(client_window, text="Nom du client:").pack(pady=5)
    entry_nom = tk.Entry(client_window)
    entry_nom.pack(pady=5)

    tk.Label(client_window, text="Entreprise:").pack(pady=5)
    entry_entreprise = tk.Entry(client_window)
    entry_entreprise.pack(pady=5)

    tk.Label(client_window, text="Personne-ressource:").pack(pady=5)
    entry_ressource = tk.Entry(client_window)
    entry_ressource.pack(pady=5)

    tk.Label(client_window, text="Adresse:").pack(pady=5)
    entry_adresse = tk.Entry(client_window)
    entry_adresse.pack(pady=5)

    tk.Label(client_window, text="Téléphone:").pack(pady=5)
    entry_telephone = tk.Entry(client_window)
    entry_telephone.pack(pady=5)

    tk.Label(client_window, text="Email:").pack(pady=5)
    entry_email = tk.Entry(client_window)
    entry_email.pack(pady=5)

    def save_client():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Clients (nom_client, entreprise, personne_ressource, adresse, telephone, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (entry_nom.get(), entry_entreprise.get(), entry_ressource.get(), entry_adresse.get(), entry_telephone.get(), entry_email.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Succès", "Client créé avec succès!")
        client_window.destroy()

    btn_save = tk.Button(client_window, text="Enregistrer", command=save_client)
    btn_save.pack(pady=20)

# Fonction pour afficher les clients (à développer)
def view_clients():
    messagebox.showinfo("Information", "Fonctionnalité en cours de développement")

# Fonction pour modifier un client (à développer)
def edit_client():
    messagebox.showinfo("Information", "Fonctionnalité en cours de développement")

# Fonction pour supprimer un client (à développer)
def delete_client():
    messagebox.showinfo("Information", "Fonctionnalité en cours de développement")

if __name__ == "__main__":
    app = create_main_window()
    app.mainloop()

