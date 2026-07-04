import customtkinter as ctk
from tkinter import messagebox

from database import update_contact


class EditContactWindow(ctk.CTkToplevel):

    def __init__(self, parent, contact_id, name, phone):
        super().__init__(parent)

        self.contact_id = contact_id

        self.title("Edit Contact")
        self.geometry("420x320")
        self.resizable(False, False)

        ctk.CTkLabel(
            self,
            text="Edit Contact",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        self.name_entry = ctk.CTkEntry(self, width=300)
        self.name_entry.pack(pady=10)
        self.name_entry.insert(0, name)

        self.phone_entry = ctk.CTkEntry(self, width=300)
        self.phone_entry.pack(pady=10)
        self.phone_entry.insert(0, phone)

        ctk.CTkButton(
            self,
            text="Update Contact",
            width=220,
            command=self.save_changes
        ).pack(pady=20)

    def save_changes(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if name == "":
            messagebox.showerror("Error", "Enter Name")
            return

        if phone == "":
            messagebox.showerror("Error", "Enter Phone Number")
            return

        update_contact(
            self.contact_id,
            name,
            phone
        )

        messagebox.showinfo(
            "Success",
            "Contact Updated Successfully"
        )

        self.destroy()