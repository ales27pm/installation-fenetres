import tkinter as tk
from tkinter import ttk, messagebox
from database import init_db, add_client, get_clients, get_client_by_id, update_client, delete_client as db_delete_client
from database import add_soumission, get_soumissions, get_soumission_by_id, update_soumission, delete_soumission

def create_main_window():
    root = tk.Tk()
    root.title("Gestion des Clients - Installation Fenêtres")

    button_frame = tk.Frame(root)
    button_frame.grid(column=0, row=0, padx=10, pady=10)

    btn_add_client = tk.Button(
        button_frame, text="Ajouter Client", command=lambda: show_add_client_form(root)
    )
    btn_add_client.grid(column=0, row=0, padx=5, pady=5)

    btn_view_clients = tk.Button(
        button_frame, text="Voir Clients", command=lambda: open_view_clients_window(root)
    )
    btn_view_clients.grid(column=1, row=0, padx=5, pady=5)

    btn_view_soumissions = tk.Button(
        button_frame, text="Voir Soumissions", command=lambda: open_view_soumissions_window(root)
    )
    btn_view_soumissions.grid(column=2, row=0, padx=5, pady=5)

    root.mainloop()

def open_view_clients_window(root):
    clients = get_clients()

    view_window = tk.Toplevel(root)
    view_window.title("Liste des Clients")

    search_label = tk.Label(view_window, text="Rechercher:")
    search_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    search_entry = tk.Entry(view_window)
    search_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    tree = ttk.Treeview(view_window, columns=('ID', 'Nom', 'Entreprise', 'Personne', 'Adresse', 'Téléphone', 'Email'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Nom', text='Nom')
    tree.heading('Entreprise', text='Entreprise')
    tree.heading('Personne', text='Personne Ressource')
    tree.heading('Adresse', text='Adresse')
    tree.heading('Téléphone', text='Téléphone')
    tree.heading('Email', text='Email')

    def update_tree(filtered_clients):
        for i in tree.get_children():
            tree.delete(i)
        for client in filtered_clients:
            tree.insert('', tk.END, values=client)

    def search_clients(*args):
        query = search_entry.get().lower()
        filtered_clients = [client for client in clients if query in client[1].lower()]
        update_tree(filtered_clients)

    search_entry.bind('<KeyRelease>', search_clients)
    update_tree(clients)

    tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    btn_edit_client = tk.Button(view_window, text="Modifier Client", command=lambda: modify_client(tree))
    btn_edit_client.grid(column=1, row=2, padx=5, pady=5)

    btn_delete_client = tk.Button(view_window, text="Supprimer Client", command=lambda: handle_delete_client(tree))
    btn_delete_client.grid(column=2, row=2, padx=5, pady=5)

    view_window.grid_columnconfigure(0, weight=1)
    view_window.grid_rowconfigure(1, weight=1)

def open_view_soumissions_window(root):
    soumissions = get_soumissions()

    view_window = tk.Toplevel(root)
    view_window.title("Liste des Soumissions")

    tree = ttk.Treeview(view_window, columns=('ID', 'Client', 'Description', 'Dimensions', 'Couleur', 'Prix', 'Date'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Client', text='Client')
    tree.heading('Description', text='Description')
    tree.heading('Dimensions', text='Dimensions')
    tree.heading('Couleur', text='Couleur')
    tree.heading('Prix', text='Prix')
    tree.heading('Date', text='Date')

    for soumission in soumissions:
        tree.insert('', tk.END, values=soumission)

    tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    btn_add_soumission = tk.Button(view_window, text="Ajouter Soumission", command=lambda: show_add_soumission_form(view_window))
    btn_add_soumission.grid(column=0, row=1, padx=5, pady=5)

    btn_edit_soumission = tk.Button(view_window, text="Modifier Soumission", command=lambda: modify_soumission(tree))
    btn_edit_soumission.grid(column=1, row=1, padx=5, pady=5)

    btn_delete_soumission = tk.Button(view_window, text="Supprimer Soumission", command=lambda: handle_delete_soumission(tree))
    btn_delete_soumission.grid(column=2, row=1, padx=5, pady=5)

    view_window.grid_columnconfigure(0, weight=1)
    view_window.grid_rowconfigure(0, weight=1)

def show_add_client_form(root):
    form_window = tk.Toplevel(root)
    form_window.title("Ajouter un Client")

    client_type = tk.StringVar(value="Particulier")

    label_type = tk.Label(form_window, text="Type de Client:")
    label_type.grid(column=0, row=0, sticky=tk.W)

    type_menu = ttk.OptionMenu(form_window, client_type, "Particulier", "Particulier", "Entreprise")
    type_menu.grid(column=1, row=0, sticky=tk.W)

    label_nom = tk.Label(form_window, text="Nom du Client:")
    label_nom.grid(column=0, row=1, sticky=tk.W)
    entry_nom = ttk.Entry(form_window)
    entry_nom.grid(column=1, row=1, sticky=tk.W)

    label_entreprise = tk.Label(form_window, text="Nom de l'Entreprise:")
    entry_entreprise = ttk.Entry(form_window)

    label_personne = tk.Label(form_window, text="Nom de la Personne Ressource:")
    entry_personne = ttk.Entry(form_window)

    label_adresse = tk.Label(form_window, text="Adresse:")
    entry_adresse = ttk.Entry(form_window)

    label_telephone = tk.Label(form_window, text="Téléphone:")
    entry_telephone = ttk.Entry(form_window)

    label_email = tk.Label(form_window, text="Email:")
    entry_email = ttk.Entry(form_window)

    def update_form(*_):
        if client_type.get() == "Entreprise":
            label_entreprise.grid(column=0, row=2, sticky=tk.W)
            entry_entreprise.grid(column=1, row=2, sticky=tk.W)
            label_personne.grid(column=0, row=3, sticky=tk.W)
            entry_personne.grid(column=1, row=3, sticky=tk.W)
        else:
            label_entreprise.grid_forget()
            entry_entreprise.grid_forget()
            label_personne.grid_forget()
            entry_personne.grid_forget()

        label_adresse.grid(column=0, row=4, sticky=tk.W)
        entry_adresse.grid(column=1, row=4, sticky=tk.W)
        label_telephone.grid(column=0, row=5, sticky=tk.W)
        entry_telephone.grid(column=1, row=5, sticky=tk.W)
        label_email.grid(column=0, row=6, sticky=tk.W)
        entry_email.grid(column=1, row=6, sticky=tk.W)

    client_type.trace_add("write", update_form)
    update_form()

    btn_save = tk.Button(
        form_window, text="Enregistrer", command=lambda: save_client(
            client_type.get(), entry_nom.get(), entry_entreprise.get(), entry_personne.get(), 
            entry_adresse.get(), entry_telephone.get(), entry_email.get()
        )
    )
    btn_save.grid(row=7, column=0, columnspan=2, pady=10)

def show_add_soumission_form(root):
    form_window = tk.Toplevel(root)
    form_window.title("Ajouter une Soumission")

    clients = get_clients()

    client_label = tk.Label(form_window, text="Client:")
    client_label.grid(column=0, row=0, sticky=tk.W)

    client_selection = ttk.Combobox(form_window, values=[client[1] for client in clients])
    client_selection.grid(column=1, row=0, sticky=tk.W)

    label_description = tk.Label(form_window, text="Description:")
    label_description.grid(column=0, row=1, sticky=tk.W)
    entry_description = ttk.Entry(form_window)
    entry_description.grid(column=1, row=1, sticky=tk.W)

    label_dimensions = tk.Label(form_window, text="Dimensions:")
    label_dimensions.grid(column=0, row=2, sticky=tk.W)
    entry_dimensions = ttk.Entry(form_window)
    entry_dimensions.grid(column=1, row=2, sticky=tk.W)

    label_couleur = tk.Label(form_window, text="Couleur:")
    label_couleur.grid(column=0, row=3, sticky=tk.W)
    entry_couleur = ttk.Entry(form_window)
    entry_couleur.grid(column=1, row=3, sticky=tk.W)

    label_prix = tk.Label(form_window, text="Prix:")
    label_prix.grid(column=0, row=4, sticky=tk.W)
    entry_prix = ttk.Entry(form_window)
    entry_prix.grid(column=1, row=4, sticky=tk.W)

    label_date = tk.Label(form_window, text="Date:")
    label_date.grid(column=0, row=5, sticky=tk.W)
    entry_date = ttk.Entry(form_window)
    entry_date.grid(column=1, row=5, sticky=tk.W)

    btn_save = tk.Button(
        form_window, text="Enregistrer", command=lambda: save_soumission(
            clients[client_selection.current()][0], entry_description.get(), entry_dimensions.get(), 
            entry_couleur.get(), entry_prix.get(), entry_date.get()
        )
    )
    btn_save.grid(row=6, column=0, columnspan=2, pady=10)

def save_client(client_type, nom, entreprise, personne, adresse, telephone, email):
    # Insertion des données avec la bonne correspondance
    if client_type == "Entreprise":
        add_client(nom, entreprise, personne, adresse, telephone, email)
    else:
        add_client(nom, "", "", adresse, telephone, email)
    messagebox.showinfo("Succès", "Le client a été ajouté avec succès.")

def save_soumission(client_id, description, dimensions, couleur, prix, date):
    add_soumission(client_id, description, dimensions, couleur, prix, date)
    messagebox.showinfo("Succès", "La soumission a été ajoutée avec succès.")

def modify_client(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un client à modifier.")
        return

    client_id = tree.item(selected_item)['values'][0]
    client = get_client_by_id(client_id)

    if client:
        show_edit_client_form(client)

def modify_soumission(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner une soumission à modifier.")
        return

    soumission_id = tree.item(selected_item)['values'][0]
    soumission = get_soumission_by_id(soumission_id)

    if soumission:
        show_edit_soumission_form(soumission)

def show_edit_client_form(client):
    form_window = tk.Toplevel()
    form_window.title("Modifier le Client")

    label_nom = tk.Label(form_window, text="Nom du Client:")
    label_nom.grid(column=0, row=0, sticky=tk.W)
    entry_nom = ttk.Entry(form_window)
    entry_nom.grid(column=1, row=0, sticky=tk.W)
    entry_nom.insert(0, client[1] if client[1] else "")

    label_entreprise = tk.Label(form_window, text="Nom de l'Entreprise:")
    entry_entreprise = ttk.Entry(form_window)
    entry_entreprise.grid(column=1, row=1, sticky=tk.W)
    entry_entreprise.insert(0, client[2] if client[2] else "")

    label_personne = tk.Label(form_window, text="Nom de la Personne Ressource:")
    entry_personne = ttk.Entry(form_window)
    entry_personne.grid(column=1, row=2, sticky=tk.W)
    entry_personne.insert(0, client[3] if client[3] else "")

    label_adresse = tk.Label(form_window, text="Adresse:")
    entry_adresse = ttk.Entry(form_window)
    entry_adresse.grid(column=1, row=3, sticky=tk.W)
    entry_adresse.insert(0, client[4] if client[4] else "")

    label_telephone = tk.Label(form_window, text="Téléphone:")
    entry_telephone = ttk.Entry(form_window)
    entry_telephone.grid(column=1, row=4, sticky=tk.W)
    entry_telephone.insert(0, client[5] if client[5] else "")

    label_email = tk.Label(form_window, text="Email:")
    entry_email = ttk.Entry(form_window)
    entry_email.grid(column=1, row=5, sticky=tk.W)
    entry_email.insert(0, client[6] if client[6] else "")

    btn_save = tk.Button(
        form_window, text="Enregistrer", command=lambda: update_client(
            client[0], entry_nom.get(), entry_entreprise.get(), entry_personne.get(), 
            entry_adresse.get(), entry_telephone.get(), entry_email.get()
        )
    )
    btn_save.grid(row=6, column=0, columnspan=2, pady=10)

def show_edit_soumission_form(soumission):
    form_window = tk.Toplevel()
    form_window.title("Modifier la Soumission")

    label_description = tk.Label(form_window, text="Description:")
    label_description.grid(column=0, row=1, sticky=tk.W)
    entry_description = ttk.Entry(form_window)
    entry_description.grid(column=1, row=1, sticky=tk.W)
    entry_description.insert(0, soumission[2] if soumission[2] else "")

    label_dimensions = tk.Label(form_window, text="Dimensions:")
    label_dimensions.grid(column=0, row=2, sticky=tk.W)
    entry_dimensions = ttk.Entry(form_window)
    entry_dimensions.grid(column=1, row=2, sticky=tk.W)
    entry_dimensions.insert(0, soumission[3] if soumission[3] else "")

    label_couleur = tk.Label(form_window, text="Couleur:")
    label_couleur.grid(column=0, row=3, sticky=tk.W)
    entry_couleur = ttk.Entry(form_window)
    entry_couleur.grid(column=1, row=3, sticky=tk.W)
    entry_couleur.insert(0, soumission[4] if soumission[4] else "")

    label_prix = tk.Label(form_window, text="Prix:")
    label_prix.grid(column=0, row=4, sticky=tk.W)
    entry_prix = ttk.Entry(form_window)
    entry_prix.grid(column=1, row=4, sticky=tk.W)
    entry_prix.insert(0, soumission[5] if soumission[5] else "")

    label_date = tk.Label(form_window, text="Date:")
    label_date.grid(column=0, row=5, sticky=tk.W)
    entry_date = ttk.Entry(form_window)
    entry_date.grid(column=1, row=5, sticky=tk.W)
    entry_date.insert(0, soumission[6] if soumission[6] else "")

    btn_save = tk.Button(
        form_window, text="Enregistrer", command=lambda: update_soumission(
            soumission[0], entry_description.get(), entry_dimensions.get(), entry_couleur.get(), 
            entry_prix.get(), entry_date.get()
        )
    )
    btn_save.grid(row=6, column=0, columnspan=2, pady=10)

def handle_delete_client(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un client à supprimer.")
        return

    client_id = tree.item(selected_item)['values'][0]

    confirm = messagebox.askyesno("Confirmer", "Êtes-vous sûr de vouloir supprimer ce client ?")
    if confirm:
        db_delete_client(client_id)
        tree.delete(selected_item)
        messagebox.showinfo("Succès", "Client supprimé avec succès.")

def handle_delete_soumission(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner une soumission à supprimer.")
        return

    soumission_id = tree.item(selected_item)['values'][0]

    confirm = messagebox.askyesno("Confirmer", "Êtes-vous sûr de vouloir supprimer cette soumission ?")
    if confirm:
        delete_soumission(soumission_id)
        tree.delete(selected_item)
        messagebox.showinfo("Succès", "Soumission supprimée avec succès.")

if __name__ == "__main__":
    init_db()
    create_main_window()

