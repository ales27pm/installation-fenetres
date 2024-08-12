import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

def create_main_window():
    root = tk.Tk()
    root.title("Gestion des Clients - Installation Fenêtres")

    button_frame = ttk.Frame(root)
    button_frame.grid(column=0, row=0, padx=10, pady=10)

    btn_add_client = ttk.Button(
        button_frame, text="Ajouter Client",
        command=lambda: show_add_client_form(root)
    )
    btn_add_client.grid(column=0, row=0, padx=5, pady=5)

    btn_view_clients = ttk.Button(
        button_frame, text="Voir Clients",
        command=view_clients
    )
    btn_view_clients.grid(column=1, row=0, padx=5, pady=5)

    btn_edit_client = ttk.Button(
        button_frame, text="Modifier Client",
        command=lambda: modify_client(root)
    )
    btn_edit_client.grid(column=2, row=0, padx=5, pady=5)

    btn_delete_client = ttk.Button(
        button_frame, text="Supprimer Client",
        command=lambda: delete_client(root)
    )
    btn_delete_client.grid(column=3, row=0, padx=5, pady=5)

    root.mainloop()

def show_add_client_form(root):
    form_window = tk.Toplevel(root)
    form_window.title("Ajouter un Client")

    client_type = tk.StringVar(value="Particulier")

    label_type = ttk.Label(form_window, text="Type de Client:")
    label_type.grid(column=0, row=0, sticky=tk.W)

    type_menu = ttk.OptionMenu(
        form_window, client_type, "Particulier", "Particulier", "Entreprise"
    )
    type_menu.grid(column=1, row=0, sticky=tk.W)
    label_nom = ttk.Label(form_window, text="Nom du Client:")
    label_nom.grid(column=0, row=1, sticky=tk.W)
    entry_nom = ttk.Entry(form_window)
    entry_nom.grid(column=1, row=1, sticky=tk.W)

    label_entreprise = ttk.Label(form_window, text="Nom de l'Entreprise:")
    entry_entreprise = ttk.Entry(form_window)

    label_personne = ttk.Label(
        form_window, text="Nom de la Personne Ressource:"
    )
    entry_personne = ttk.Entry(form_window)

    label_adresse = ttk.Label(form_window, text="Adresse:")
    entry_adresse = ttk.Entry(form_window)

    label_telephone = ttk.Label(form_window, text="Téléphone:")
    label_telephone.grid(column=0, row=4, sticky=tk.W)
    entry_telephone = ttk.Entry(form_window)
    entry_telephone.grid(column=1, row=4, sticky=tk.W)

    label_email = ttk.Label(form_window, text="Email:")
    label_email.grid(column=0, row=5, sticky=tk.W)
    entry_email = ttk.Entry(form_window)
    entry_email.grid(column=1, row=5, sticky=tk.W)

    def update_form(*_):
        if client_type.get() == "Entreprise":
            label_entreprise.grid(column=0, row=2, sticky=tk.W)
            entry_entreprise.grid(column=1, row=2, sticky=tk.W)
            label_personne.grid(column=0, row=3, sticky=tk.W)
            entry_personne.grid(column=1, row=3, sticky=tk.W)
            label_adresse.grid(column=0, row=4, sticky=tk.W)
            entry_adresse.grid(column=1, row=4, sticky=tk.W)
            label_telephone.grid(column=0, row=5, sticky=tk.W)
            entry_telephone.grid(column=1, row=5, sticky=tk.W)
            label_email.grid(column=0, row=6, sticky=tk.W)
            entry_email.grid(column=1, row=6, sticky=tk.W)
        else:
            label_entreprise.grid_forget()
            entry_entreprise.grid_forget()
            label_personne.grid_forget()
            entry_personne.grid_forget()
            label_adresse.grid(column=0, row=2, sticky=tk.W)
            entry_adresse.grid(column=1, row=2, sticky=tk.W)
            label_telephone.grid(column=0, row=3, sticky=tk.W)
            entry_telephone.grid(column=1, row=3, sticky=tk.W)
            label_email.grid(column=0, row=4, sticky=tk.W)
            entry_email.grid(column=1, row=4, sticky=tk.W)
    client_type.trace_add("write", update_form)

    btn_save = ttk.Button(
        form_window, text="Enregistrer",
        command=lambda: save_client(
            client_type.get(), entry_nom.get(), entry_entreprise.get(),
            entry_personne.get(), entry_adresse.get(), entry_telephone.get(),
            entry_email.get()
        )
    )
    btn_save.grid(column=0, row=7, columnspan=2, pady=10)

def save_client(client_type, nom, entreprise, personne, adresse, telephone, email):
    db_path = os.path.join('/home/kali/installation-fenetres/data', 'clients.db')
    print(f"Connecting to database at {db_path}")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO clients (nom, entreprise, personne_ressource, adresse, telephone, email)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nom, entreprise, personne, adresse, telephone, email))

    conn.commit()
    conn.close()
    messagebox.showinfo("Succès", "Le client a été ajouté avec succès.")

def get_clients():
    db_path = os.path.join('/home/kali/installation-fenetres/data', 'clients.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()

    conn.close()
    return clients

def view_clients():
    clients = get_clients()

    window = tk.Toplevel()
    window.title("Liste des Clients")

    tree = ttk.Treeview(window, columns=('ID', 'Nom', 'Entreprise', 'Personne', 'Adresse', 'Téléphone', 'Email'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Nom', text='Nom')
    tree.heading('Entreprise', text='Entreprise')
    tree.heading('Personne', text='Personne Ressource')
    tree.heading('Adresse', text='Adresse')
    tree.heading('Téléphone', text='Téléphone')
    tree.heading('Email', text='Email')

    for client in clients:
        tree.insert('', tk.END, values=client)

    tree.pack(expand=True, fill=tk.BOTH)

def modify_client(root):
    window = tk.Toplevel(root)
    window.title("Modifier Client")
    # Implement the logic to modify a client here

def delete_client(root):
    window = tk.Toplevel(root)
    window.title("Supprimer Client")
    # Implement the logic to delete a client here
