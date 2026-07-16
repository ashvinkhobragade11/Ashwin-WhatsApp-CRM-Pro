import customtkinter as ctk

from tkinter import messagebox
from modules.auth.user_manager import reset_user_password


class ResetPasswordWindow(ctk.CTkToplevel):

    def __init__(
        self,
        master,
        username
    ):
        super().__init__(master)

        self.username = username

        self.title("Reset Password")
        self.geometry("450x350")

        ctk.CTkLabel(
            self,
            text="Reset Password",
            font=("Arial", 24, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            self,
            text=f"Username : {username}"
        ).pack(pady=10)

        ctk.CTkLabel(
            self,
            text="New Password"
        ).pack(pady=(15, 5))

        self.password = ctk.CTkEntry(
            self,
            show="*"
        )
        self.password.pack(
            padx=30,
            fill="x"
        )

        ctk.CTkLabel(
            self,
            text="Confirm Password"
        ).pack(pady=(15, 5))

        self.confirm_password = ctk.CTkEntry(
            self,
            show="*"
        )
        self.confirm_password.pack(
            padx=30,
            fill="x"
        )

        ctk.CTkButton(
            self,
            text="Reset Password",
            command=self.reset_password
        ).pack(
            pady=30
        )

    def reset_password(self):

        print("Reset Password Button Clicked")

        password = self.password.get().strip()
        confirm = self.confirm_password.get().strip()

        print("Password =", repr(password))
        print("Confirm =", repr(confirm))

        if password == "":
            messagebox.showerror(
                "Error",
                "Please enter new password."
            )
            return

        if confirm == "":
            messagebox.showerror(
                "Error",
                "Please confirm password."
            )
            return

        if len(password) < 8:
            messagebox.showerror(
                "Error",
                "Password must be at least 8 characters long."
            )
            return

        if password != confirm:
            messagebox.showerror(
                "Error",
                "Passwords do not match."
            )
            return

        reset_user_password(
            self.username,
            password
        )

        messagebox.showinfo(
            "Success",
            "Password reset successfully."
        )

        self.destroy()