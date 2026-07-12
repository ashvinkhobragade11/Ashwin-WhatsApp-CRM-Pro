import customtkinter as ctk


class UsersPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="User Management",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(30, 20))

        ctk.CTkLabel(
            self,
            text="🚧 User Management Module is under development.",
            font=("Arial", 18)
        ).pack(pady=20)