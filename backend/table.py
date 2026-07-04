import tkinter as tk
from tkinter import ttk
from backend.database import load_contacts

def open_contact_table():

    window = tk.Toplevel()

    window.title("Contact List")
    window.geometry("650x400")

    tree = ttk.Treeview(
        window,
        columns=("Name", "Phone"),
        show="headings"
    )

    tree.heading("Name", text="Name")
    tree.heading("Phone", text="Phone Number")

    tree.column("Name", width=250)
    tree.column("Phone", width=250)

    contacts = load_contacts()

    for contact in contacts:
        tree.insert(
            "",
            tk.END,
            values=(
                contact["name"],
                contact["phone"]
            )
        )

    tree.pack(fill="both", expand=True, padx=10, pady=10)