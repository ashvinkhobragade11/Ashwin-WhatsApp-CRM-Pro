from backend.forms import open_add_contact, open_search_contact
from backend.table import open_contact_table
import tkinter as tk

from backend.contact import (
    show_contacts,
    search_contact,
    update_contact,
    delete_contact,
    export_contacts
)

from backend.forms import open_add_contact

window = tk.Tk()
window.title("WhatsApp CRM")
window.geometry("700x500")
window.configure(bg="white")

title = tk.Label(
    window,
    text="WhatsApp CRM",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="green"
)
title.pack(pady=20)

btn_add = tk.Button(
    window,
    text="➕ Add Contact",
    width=25,
    height=2,
    command=open_add_contact
)
btn_add.pack(pady=5)

btn_list = tk.Button(
    window,
    text="📋 Contact List",
    width=25,
    height=2,
   command=open_contact_table
)
btn_list.pack(pady=5)

btn_search = tk.Button(
    window,
    text="🔍 Search Contact",
    width=25,
    height=2,
    command=open_search_contact
)
btn_search.pack(pady=5)

btn_update = tk.Button(
    window,
    text="✏ Update Contact",
    width=25,
    height=2,
    command=update_contact
)
btn_update.pack(pady=5)

btn_delete = tk.Button(
    window,
    text="🗑 Delete Contact",
    width=25,
    height=2,
    command=delete_contact
)
btn_delete.pack(pady=5)

btn_export = tk.Button(
    window,
    text="📤 Export Contacts",
    width=25,
    height=2,
    command=export_contacts
)
btn_export.pack(pady=5)

window.mainloop()