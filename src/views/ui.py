"""
Module pour la gestion de l'interface utilisateur de l'application 'Installation Fenêtres'.
Contient les fonctions pour créer les fenêtres principales et gérer les entrées utilisateur.
"""

import tkinter as tk
from tkinter import ttk


def create_main_window():
    """
    Crée la fenêtre principale de l'application et initialise les champs de saisie
    pour la gestion des clients, qu'ils soient des entreprises ou des particuliers.
    """
    root = tk.Tk()
    root.title("Gestion des Clients - Installation Fenêtres")

    # Section des boutons principaux
    button_frame = ttk.Frame(root)
    button_frame.grid(column=0, row=0, padx=10, pady=10)

    btn_add_client = ttk.Button(
        button_frame, text="Ajouter Client",
        command=lambda: show_add_client_form(root)
    )
    btn_add_client.grid(column=0, row=0, padx=5, pady=5)

    btn_view_clients = ttk.Button(
        button_frame, text="Voir Clients",
        command=lambda: view_clients(root)
    )
    btn_view_clients.grid(column=1, row=0, padx=5, pady=5)

    btn_edit_client = ttk.Button(
        button_frame, text="Modifier Client",
        command=lambda: edit_client(root)
    )
    btn_edit_client.grid(column=2, row=0, padx=5, pady=5)

    btn_delete_client = ttk.Button(
        button_frame, text="Supprimer Client",
        command=lambda: delete_client(root)
    )
    btn_delete_client.grid(column=3, row=0, padx=5, pady=5)

    root.mainloop()


def show_add_client_form(root):
    """
    Affiche le formulaire pour ajouter un nouveau client, avec des champs
    différents selon qu'il s'agit d'un particulier ou d'une entreprise.
    """
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
    entry_adresse.grid(column=1, row=3, sticky=tk.W)

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
        form_window, text="Sauvegarder",
        command=lambda: save_client(
            client_type.get(), entry_nom.get(), entry_entreprise.get(),
            entry_personne.get(), entry_adresse.get(), entry_telephone.get(),
            entry_email.get()
        )
    )
    btn_save.grid(column=0, row=7, columnspan=2, pady=10)


def save_client(client_type, nom, entreprise, personne, adresse, telephone, email):
    """
    Fonction pour sauvegarder les informations du client.
    """
    # Ici, tu implémenterais la logique pour sauvegarder les données
    # dans ta base de données ou un fichier.
    print(f"Client sauvegardé : {client_type}, {nom}, {entreprise}, {personne}, "
          f"{adresse}, {telephone}, {email}")


def view_clients(_):
    """
    Fonction pour voir la liste des clients (à implémenter).
    """
    print("Afficher la liste des clients")


def edit_client(_):
    """
    Fonction pour éditer un client (à implémenter).
    """
    print("Modifier un client")


def delete_client(_):
    """
    Fonction pour supprimer un client (à implémenter).
    """
    print("Supprimer un client")


if __name__ == "__main__":
    create_main_window()
