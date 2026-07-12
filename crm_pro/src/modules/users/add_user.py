import customtkinter as ctk
from tkinter import messagebox

from modules.auth.user_manager import create_user


class AddUserWindow(ctk.CTkToplevel):

    def __init__(self, master, refresh_callback):
        self.refresh_callback = refresh_callback
        super().__init__(master)

        self.title("Add User")
        self.geometry("450x500")

        ctk.CTkLabel(
            self,
            text="Add User",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        self.username = ctk.CTkEntry(
            self,
            placeholder_text="Username"
        )
        self.username.pack(pady=10, padx=30, fill="x")

        self.password = ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10, padx=30, fill="x")

        self.full_name = ctk.CTkEntry(
            self,
            placeholder_text="Full Name"
        )
        self.full_name.pack(pady=10, padx=30, fill="x")

        self.role = ctk.CTkComboBox(
            self,
            values=[
                "Admin",
                "Manager",
                "Executive"
            ]
        )
        self.role.pack(pady=10, padx=30, fill="x")

        self.status = ctk.CTkComboBox(
            self,
            values=[
                "Active",
                "Inactive"
            ]
        )
        self.status.pack(pady=10, padx=30, fill="x")

        ctk.CTkButton(
            self,
            text="Save User",
            command=self.save_user
        ).pack(pady=25)

    def save_user(self):

        username = self.username.get().strip()
        password = self.password.get().strip()
        full_name = self.full_name.get().strip()
        role = self.role.get()
        status = self.status.get()

        success = create_user(
            username,
            password,
            full_name,
            role,
            status
        )

        if not success:
            messagebox.showerror(
                "Error",
                "Username already exists."
            )
            return

        messagebox.showinfo(
            "Success",
            "User created successfully."
        )

        self.refresh_callback()

        self.destroy()