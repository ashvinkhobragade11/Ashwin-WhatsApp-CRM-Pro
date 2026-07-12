import customtkinter as ctk
from tkinter import ttk, messagebox

from database import get_contacts
from modules.contacts.add_contact import AddContactWindow
from modules.contacts.edit_contact import EditContactWindow
from modules.contacts.delete_contact import DeleteContactWindow
from modules.contacts.search_contact import search
from modules.contacts.export_contacts import export_contacts
from modules.contacts.import_contacts import import_contacts


class ContactsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Contact Management",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        top_frame = ctk.CTkFrame(self)
        top_frame.pack(fill="x", padx=20)

        self.search_entry = ctk.CTkEntry(
            top_frame,
            placeholder_text="Search Contact..."
        )
        self.search_entry.pack(side="left", padx=10, pady=10)

        ctk.CTkButton(
            top_frame,
            text="Search",
            command=self.search_contacts
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            top_frame,
            text="Refresh",
            command=self.load_contacts
        ).pack(side="right", padx=10)

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("ID", "Name", "Phone"),
            show="headings"
        )

        self.tree.heading("ID", text="SR No.")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Mobile Number")

        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Name", width=300)
        self.tree.column("Phone", width=220)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", self.on_double_click)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20, pady=10)

        ctk.CTkButton(
            button_frame,
            text="Add Contact",
            command=self.open_add_contact
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="Edit",
            command=self.open_edit_contact
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="Delete",
            command=self.open_delete_contact
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            button_frame,
            text="Import",
            command=import_contacts
        ).pack(side="right", padx=5)

        ctk.CTkButton(
            button_frame,
            text="Export",
            command=export_contacts
        ).pack(side="right", padx=5)

        self.load_contacts()
    def open_add_contact(self):
        AddContactWindow(self)
        self.after(500, self.load_contacts)

    def on_double_click(self, event):
        self.open_edit_contact()

    def open_edit_contact(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Selection Required",
                "Please select a contact."
            )
            return

        values = self.tree.item(selected[0])["values"]

        EditContactWindow(
            self,
            values[0],
            values[1],
            values[2]
        )

        self.after(500, self.load_contacts)

    def open_delete_contact(self):

        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Selection Required",
                "Please select a contact."
            )
            return

        values = self.tree.item(selected[0])["values"]

        DeleteContactWindow(
            self,
            values[0]
        )

        self.after(500, self.load_contacts)

    def search_contacts(self):

        keyword = self.search_entry.get().strip()

        for row in self.tree.get_children():
            self.tree.delete(row)

        contacts = search(keyword)

        for contact in contacts:
            self.tree.insert(
                "",
                "end",
                values=contact
            )

    def load_contacts(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        contacts = get_contacts()

        for contact in contacts:
            self.tree.insert(
                "",
                "end",
                values=contact
            )