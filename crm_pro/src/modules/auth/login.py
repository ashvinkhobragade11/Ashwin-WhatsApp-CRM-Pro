import customtkinter as ctk
from tkinter import messagebox

from database import connect
from modules.auth.password_manager import verify_password
from modules.auth.user_manager import get_user


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Ashwin WhatsApp CRM Pro")
        self.geometry("500x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("green")

        self.build_ui()

    def build_ui(self):

        ctk.CTkLabel(
            self,
            text="Ashwin WhatsApp CRM Pro",
            font=("Arial", 28, "bold")
        ).pack(pady=(50, 10))

        ctk.CTkLabel(
            self,
            text="Enterprise Edition",
            font=("Arial", 16)
        ).pack(pady=(0, 30))

        self.username = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            self,
            width=320,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.login_btn = ctk.CTkButton(
            self,
            text="Login",
            command=self.login
        )
        self.login_btn.pack(pady=25)

        self.exit_btn = ctk.CTkButton(
            self,
            text="Exit",
            fg_color="gray",
            command=self.destroy
        )
        self.exit_btn.pack()

        ctk.CTkLabel(
            self,
            text="Version 0.8",
            font=("Arial", 12)
        ).pack(side="bottom", pady=20)

    def login(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        # Username Validation
        if username == "":
            messagebox.showerror(
                "Login Error",
                "Please enter username."
            )
            return

        # Password Validation
        if password == "":
            messagebox.showerror(
                "Login Error",
                "Please enter password."
            )
            return

        # Fetch User
        user = get_user(username)

        if user is None:
            messagebox.showerror(
                "Login Error",
                "Invalid Username or Password"
            )
            return

        # Verify Password
        stored_hash = user[1]

        if not verify_password(password, stored_hash):
            messagebox.showerror(
                "Login Error",
                "Invalid Username or Password"
            )
            return

        # Login Success
        messagebox.showinfo(
            "Success",
            "Login Successful"
        )


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()