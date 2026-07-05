import customtkinter as ctk

from modules.dashboard.statistics import dashboard_statistics


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        stats = dashboard_statistics()

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=25)

        self.total_card = ctk.CTkFrame(
            self,
            width=300,
            height=140
        )
        self.total_card.pack(pady=20)

        ctk.CTkLabel(
            self.total_card,
            text="👥 Total Contacts",
            font=("Arial", 22, "bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            self.total_card,
            text=str(stats["total_contacts"]),
            font=("Arial", 40, "bold")
        ).pack()