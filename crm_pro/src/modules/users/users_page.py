import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox

from modules.auth.user_manager import deactivate_user
from database import get_users
from modules.users.add_user import AddUserWindow
from modules.users.edit_user import EditUserWindow


class UsersPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="User Management",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=20)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(fill="x", padx=20)

        ctk.CTkButton(
            button_frame,
            text="Add User",
            width=150,
            command=self.open_add_user
        ).pack(side="left", pady=10)

        ctk.CTkButton(
            button_frame,
            text="✏️ Edit User",
            command=self.open_edit_user
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            button_frame,
            text="Disable User",
            fg_color="orange",
            hover_color="#cc8400",
            command=self.disable_user
        ).pack(
            side="left",
            padx=10
        )

        table_frame = ctk.CTkFrame(self)
        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=("Username", "Role", "Status"),
            show="headings"
        )

        self.tree.heading("Username", text="Username")
        self.tree.heading("Role", text="Role")
        self.tree.heading("Status", text="Status")

        self.tree.column("Username", width=250)
        self.tree.column("Role", width=180)
        self.tree.column("Status", width=180)

        self.tree.pack(
            fill="both",
            expand=True
        )

        self.load_users()

    def load_users(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        users = get_users()

        for user in users:
            self.tree.insert(
                "",
                "end",
                values=user
            )

    def open_add_user(self):

        AddUserWindow(
            self,
            self.load_users
        )

    def open_edit_user(self):

        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(selected[0])["values"]

        EditUserWindow(
            self,
            values[0],
            values[1],
            values[2],
            self.load_users
        )

    def disable_user(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "Warning",
                "Please select a user."
            )
            return

        values = self.tree.item(selected[0])["values"]

        username = values[0]

        confirm = messagebox.askyesno(
            "Disable User",
            f"Disable user '{username}'?"
        )

        if not confirm:
            return

        deactivate_user(username)

        messagebox.showinfo(
            "Success",
            "User disabled successfully."
        )

        self.load_users()