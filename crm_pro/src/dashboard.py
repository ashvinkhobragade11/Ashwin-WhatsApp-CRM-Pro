import customtkinter as ctk
from tkinter import messagebox

from modules.users.users_page import UsersPage
from modules.reports.reports_page import ReportsPage
from contacts import ContactsPage
from modules.contacts.edit_contact import EditContactWindow
from modules.dashboard.dashboard_page import DashboardPage
from modules.dashboard.activity import get_recent_activities
from modules.auth.session_manager import (
    get_current_user,
    destroy_session
)

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")


class Dashboard(ctk.CTk):

    def show_users(self):
        self.clear_main()
        UsersPage(self.main)

    def show_reports(self):
        self.clear_main()
        ReportsPage(self.main)


    def __init__(self):
        super().__init__()

        self.title("Ashwin WhatsApp CRM Pro")
        self.geometry("1400x800")

        # Current Logged-in User
        self.current_user = get_current_user()

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220)
        self.sidebar.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self.sidebar,
            text="WhatsApp CRM",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        # User Information
        if self.current_user:

            welcome = ctk.CTkLabel(
                self.sidebar,
                text=f"Welcome\n{self.current_user[0]}",
                font=("Arial", 16, "bold")
            )
            welcome.pack(pady=10)

            role = ctk.CTkLabel(
                self.sidebar,
                text=f"Role : {self.current_user[2]}"
            )
            role.pack()

            status = ctk.CTkLabel(
                self.sidebar,
                text=f"Status : {self.current_user[3]}"
            )
            status.pack(pady=(0, 20))

        # Sidebar Buttons
        self.btn_dashboard = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            command=self.show_dashboard
        )
        self.btn_dashboard.pack(pady=8)

        self.btn_contacts = ctk.CTkButton(
            self.sidebar,
            text="Contacts",
            command=self.show_contacts
        )
        self.btn_contacts.pack(pady=8)

        self.btn_campaigns = ctk.CTkButton(
            self.sidebar,
            text="Campaigns"
        )
        self.btn_campaigns.pack(pady=8)

        self.btn_reports = ctk.CTkButton(
            self.sidebar,
            text="Reports",
            command=self.show_reports
        )
        self.btn_reports.pack(pady=8)

        self.btn_users = ctk.CTkButton(
            self.sidebar,
            text="Users",
            command=self.show_users
        )
        self.btn_users.pack(pady=8)

        self.btn_settings = ctk.CTkButton(
            self.sidebar,
            text="Settings"
        )
        self.btn_settings.pack(pady=8)

        self.btn_logout = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            fg_color="red",
            hover_color="#b22222",
            command=self.logout
        )
        self.btn_logout.pack(pady=20)

        # Main Frame
        self.main = ctk.CTkFrame(self)
        self.main.pack(fill="both", expand=True)

        self.show_dashboard()

    def clear_main(self):
        for widget in self.main.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main()
        DashboardPage(self.main)

    def show_contacts(self):
        self.clear_main()
        ContactsPage(self.main)

    def logout(self):
        messagebox.showinfo(
            "Logout",
            "Logout feature is under development."
    )

if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()