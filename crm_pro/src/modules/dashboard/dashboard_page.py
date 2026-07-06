import customtkinter as ctk

from modules.dashboard.statistics import dashboard_statistics
from modules.dashboard.activity import get_recent_activities


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        stats = dashboard_statistics()
        activities = get_recent_activities()

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=25)

        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards_frame.pack(pady=20)

        self.total_card = self.create_stat_card(
            cards_frame,
            "👥 Total Contacts",
            stats["total_contacts"]
        )

        self.total_card.grid(
            row=0,
            column=0,
            padx=15,
            pady=15
        )
        
        self.today_card = self.create_stat_card(
            cards_frame,
            "📅 Today's Contacts",
            stats.get("today_contacts", 0)
        )

        self.today_card.grid(
            row=0,
            column=1,
            padx=15,
            pady=15
        )
        activity_frame = ctk.CTkFrame(
            self
        )
        activity_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        ctk.CTkLabel(
            activity_frame,
            text="📋 Recent Activity",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )
        if not activities:

            ctk.CTkLabel(
                activity_frame,
                text="No Activity Yet",
                font=("Arial", 16)
            ).pack(
                anchor="w",
                padx=20,
                pady=5
            )

        else:

            for activity in activities:

                ctk.CTkLabel(
                    activity_frame,
                    text=activity,
                    font=("Arial", 16)
                ).pack(
                    anchor="w",
                    padx=20,
                    pady=3
                )

    def create_stat_card(
        self,
        parent,
        title,
        value
    ):

        card = ctk.CTkFrame(
            parent,
            width=260,
            height=140
        )

        ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 10))

        ctk.CTkLabel(
            card,
            text=str(value),
            font=("Arial", 38, "bold")
        ).pack()

        return card