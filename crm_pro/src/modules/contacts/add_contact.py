import customtkinter as ctk
from tkinter import messagebox
from database import add_contact

class AddContactWindow(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Add Contact")
        self.geometry("420x320")
        self.resizable(False, False)

        ctk.CTkLabel(
            self,
            text="Add New Contact",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        self.name_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Full Name"
        )
        self.name_entry.pack(pady=10)

        self.phone_entry = ctk.CTkEntry(
            self,
            width=300,
            placeholder_text="Phone Number"
        )
        self.phone_entry.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Save Contact",
            width=220,
            command=self.save_contact
        ).pack(pady=25)

    def save_contact(self):

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if name == "":
            messagebox.showerror("Error", "Enter Name")
            return

        if phone == "":
            messagebox.showerror("Error", "Enter Phone Number")
            return
        
        add_contact(name, phone)

        messagebox.showinfo(
            "Success",
            "Contact Saved Successfully"
        )

        self.destroy()