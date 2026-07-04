import customtkinter as ctk
from tkinter import messagebox

from database import delete_contact


class DeleteContactWindow(ctk.CTkToplevel):

    def __init__(self, parent, contact_id):
        super().__init__(parent)

        self.contact_id = contact_id

        self.title("Delete Contact")
        self.geometry("400x180")
        self.resizable(False, False)

        ctk.CTkLabel(
            self,
            text="Delete Contact",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        ctk.CTkLabel(
            self,
            text="Are you sure you want to delete this contact?"
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="Yes, Delete",
            fg_color="red",
            command=self.delete
        ).pack(pady=15)

    def delete(self):

        delete_contact(self.contact_id)

        messagebox.showinfo(
            "Success",
            "Contact Deleted Successfully"
        )

        self.destroy()