import customtkinter as ctk
from contacts import ContactsPage

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("green")


class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Ashwin WhatsApp CRM Pro")
        self.geometry("1400x800")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=220)
        self.sidebar.pack(side="left", fill="y")

        title = ctk.CTkLabel(
            self.sidebar,
            text="WhatsApp CRM",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

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
            text="Reports"
        )
        self.btn_reports.pack(pady=8)

        self.btn_settings = ctk.CTkButton(
            self.sidebar,
            text="Settings"
        )
        self.btn_settings.pack(pady=8)

        self.main = ctk.CTkFrame(self)
        self.main.pack(fill="both", expand=True)

        self.show_dashboard()

    def clear_main(self):
        for widget in self.main.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_main()

        ctk.CTkLabel(
            self.main,
            text="Dashboard",
            font=("Arial", 30, "bold")
        ).pack(pady=30)

        ctk.CTkLabel(
            self.main,
            text="Welcome to Ashwin WhatsApp CRM Pro",
            font=("Arial", 20)
        ).pack(pady=10)

    def show_contacts(self):
        self.clear_main()
        ContactsPage(self.main)