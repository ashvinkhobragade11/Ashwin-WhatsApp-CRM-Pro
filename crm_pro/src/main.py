from database import create_table
from database import create_users_table

from modules.auth.user_manager import create_default_admin

from controllers.application_controller import ApplicationController


def main():

    create_table()

    create_users_table()

    create_default_admin()

    controller = ApplicationController()

    controller.initialize()

    controller.show_login()


if __name__ == "__main__":
    main()