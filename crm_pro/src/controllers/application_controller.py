from modules.auth.login import LoginWindow


class ApplicationController:

    def initialize(self):
        """
        Future:
        Logging
        Configuration
        Services
        """
        pass

    def show_login(self):

        app = LoginWindow()

        app.mainloop()