from menu import show_menu
from contact import (
    add_contact,
    show_contacts,
    delete_contact,
    search_contact,
    update_contact,
    export_contacts
)
from login import login

if login():
    show_menu()

    choice = input("Choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        show_contacts()

    elif choice == "3":
        delete_contact()

    elif choice == "4":
        search_contact()

    elif choice == "5":
        update_contact()

    elif choice == "6":
        export_contacts()

    elif choice == "7":
        print("Bye...")

    else:
        print("Invalid Choice")