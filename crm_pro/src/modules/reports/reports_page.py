import customtkinter as ctk


class ReportsPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Reports",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=(30, 20))

        message = ctk.CTkLabel(
            self,
            text="🚧 Reports Module is under development.",
            font=("Arial", 18)
        )
        message.pack(pady=20)