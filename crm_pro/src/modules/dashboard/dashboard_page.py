import customtkinter as ctk

from modules.dashboard.statistics import dashboard_statistics
from modules.dashboard.activity import get_recent_activities


class DashboardPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True)

        stats = dashboard_statistics()
        activities = get_recent_activities()

        # ================= Title =================
        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        title.pack(pady=25)

        # ================= Statistics Cards =================
        cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        cards_frame.pack(pady=20)

        # Total Contacts
        self.total_card = self.create_stat_card(
            cards_frame,
            "👥 Total Contacts",
            stats.get("total_contacts", 0)
        )
        self.total_card.grid(row=0, column=0, padx=15, pady=15)

        # Today's Contacts
        self.today_card = self.create_stat_card(
            cards_frame,
            "📅 Today's Contacts",
            stats.get("today_contacts", 0)
        )
        self.today_card.grid(row=0, column=1, padx=15, pady=15)

        # Total Exports
        self.export_card = self.create_stat_card(
            cards_frame,
            "📤 Total Exports",
            stats.get("total_exports", 0)
        )
        self.export_card.grid(row=0, column=2, padx=15, pady=15)

        # Total Imports
        self.import_card = self.create_stat_card(
            cards_frame,
            "📥 Total Imports",
            stats.get("total_imports", 0)
        )
        self.import_card.grid(row=0, column=3, padx=15, pady=15)

        # ================= Recent Activity =================
        quick_frame = ctk.CTkFrame(self)
        quick_frame.pack(
            fill="x",
            padx=25,
         pady=10
        )

        ctk.CTkLabel(
            quick_frame,
            text="⚡ Quick Actions",
            font=("Arial", 22, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        buttons_frame = ctk.CTkFrame(
            quick_frame,
            fg_color="transparent"
        )
        buttons_frame.pack(pady=10)

        ctk.CTkButton(
            buttons_frame,
            text="➕ Add Contact",
            width=180
        ).pack(
            side="left",
            padx=10
        )

        ctk.CTkButton(
            buttons_frame,
            text="📋 Contacts",
            width=180
        ).pack(
            side="left",
            padx=10
        )
        
        activity_frame = ctk.CTkFrame(self)
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

    def create_stat_card(self, parent, title, value):

        card = ctk.CTkFrame(
            parent,
            width=260,
            height=140
        )

        card.grid_propagate(False)

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