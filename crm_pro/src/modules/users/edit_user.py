import customtkinter as ctk
from tkinter import messagebox

from modules.auth.user_manager import edit_user


class EditUserWindow(ctk.CTkToplevel):

    def __init__(
        self,
        master,
        username,
        role,
        status,
        refresh_callback
    ):
        self.refresh_callback = refresh_callback

        super().__init__(master)

        self.title("Edit User")
        self.geometry("450x420")

        # Username
        ctk.CTkLabel(
            self,
            text="Username"
        ).pack(pady=(20, 5))

        self.username = ctk.CTkEntry(self)
        self.username.pack(
            padx=30,
            fill="x"
        )

        self.username.insert(0, username)
        self.username.configure(state="disabled")

        # Role
        ctk.CTkLabel(
            self,
            text="Role"
        ).pack(pady=(15, 5))

        self.role = ctk.CTkComboBox(
            self,
            values=[
                "Admin",
                "Manager",
                "Executive"
            ]
        )

        self.role.pack(
            padx=30,
            fill="x"
        )

        self.role.set(role)

        # Status
        ctk.CTkLabel(
            self,
            text="Status"
        ).pack(pady=(15, 5))

        self.status = ctk.CTkComboBox(
            self,
            values=[
                "Active",
                "Inactive"
            ]
        )

        self.status.pack(
            padx=30,
            fill="x"
        )

        self.status.set(status)

        # Save Button
        ctk.CTkButton(
            self,
            text="Save Changes",
            command=self.save_changes
        ).pack(
            pady=30
        )

    def save_changes(self):

        username = self.username.get()
        role = self.role.get()
        status = self.status.get()

        edit_user(
            username,
            role,
            status
        )

        messagebox.showinfo(
            "Success",
            "User updated successfully."
        )

        self.refresh_callback()

        self.destroy()