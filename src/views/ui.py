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
        command=lambda: view_clients()
    )
    btn_view_clients.grid(column=1, row=0, padx=5, pady=5)

    btn_edit_client = ttk.Button(
        button_frame, text="Modifier Client",
        command=lambda: modify_client()
    )
    btn_edit_client.grid(column=2, row=0, padx=5, pady=5)

    btn_delete_client = ttk.Button(
        button_frame, text="Supprimer Client",
        command=lambda: delete_client()
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

    # Bouton de sauvegarde
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


def modify_client():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un client à modifier.")
        return

    client_id = tree.item(selected_item)['values'][0]

    db_path = os.path.join('/home/kali/installation-fenetres/data', 'clients.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clients WHERE id=?", (client_id,))
    client = cursor.fetchone()
    conn.close()

    if client:
        modify_window = tk.Toplevel()
        modify_window.title("Modifier le Client")

        tk.Label(modify_window, text="Nom du Client:").grid(row=0, column=0)
        entry_nom = tk.Entry(modify_window)
        entry_nom.grid(row=0, column=1)

        tk.Label(modify_window, text="Nom de l'Entreprise:").grid(row=1, column=0)
        entry_entreprise = tk.Entry(modify_window)
        entry_entreprise.grid(row=1, column=1)

        tk.Label(modify_window, text="Personne Ressource:").grid(row=2, column=0)
        entry_personne = tk.Entry(modify_window)
        entry_personne.grid(row=2, column=1)

        tk.Label(modify_window, text="Adresse:").grid(row=3, column=0)
        entry_adresse = tk.Entry(modify_window)
        entry_adresse.grid(row=3, column=1)

        tk.Label(modify_window, text="Téléphone:").grid(row=4, column=0)
        entry_telephone = tk.Entry(modify_window)
        entry_telephone.grid(row=4, column=1)

        tk.Label(modify_window, text="Email:").grid(row=5, column=0)
        entry_email = tk.Entry(modify_window)
        entry_email.grid(row=5, column=1)

        entry_nom.insert(0, client[1])
        entry_entreprise.insert(0, client[2])
        entry_personne.insert(0, client[3])
        entry_adresse.insert(0, client[4])
        entry_telephone.insert(0, client[5])
        entry_email.insert(0, client[6])

        def save_changes():
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE clients
                SET nom=?, entreprise=?, personne_ressource=?, adresse=?, telephone=?, email=?
                WHERE id=?
            ''', (entry_nom.get(), entry_entreprise.get(), entry_personne.get(),
                  entry_adresse.get(), entry_telephone.get(), entry_email.get(), client_id))

            conn.commit()
            conn.close()
            messagebox.showinfo("Succès", "Les informations du client ont été mises à jour.")
            modify_window.destroy()

        btn_save_changes = ttk.Button(modify_window, text="Enregistrer les modifications", command=save_changes)
        btn_save_changes.grid(row=6, column=0, columnspan=2, pady=10)

    else:
        messagebox.showerror("Erreur", "Client non trouvé.")


def delete_client():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un client à supprimer.")
        return

    client_id = tree.item(selected_item)['values'][0]

    confirm = messagebox.askyesno("Confirmer", "Êtes-vous sûr de vouloir supprimer ce client?")
    if confirm:
        db_path = os.path.join('/home/kali/installation-fenetres/data', 'clients.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM clients WHERE id=?", (client_id,))
        conn.commit()
        conn.close()

        tree.delete(selected_item)
        messagebox.showinfo("Succès", "Client supprimé avec succès.")
