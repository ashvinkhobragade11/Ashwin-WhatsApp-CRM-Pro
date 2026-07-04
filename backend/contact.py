import csv
from backend.database import load_contacts, save_contacts

contacts = load_contacts()


def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact Added Successfully")


def show_contacts():
    print("\n===== Contact List =====")

    for contact in contacts:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("----------------")


def delete_contact():
    phone = input("Delete Phone Number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact Deleted Successfully")
            return

    print("Contact Not Found")


def search_contact():
    phone = input("Search Phone Number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print("\n===== Contact Found =====")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            return

    print("Contact Not Found")


def update_contact():
    phone = input("Old Phone Number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            contact["name"] = input("New Name: ")
            contact["phone"] = input("New Phone: ")
            save_contacts(contacts)
            print("Contact Updated Successfully")
            return

    print("Contact Not Found")


def export_contacts():
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Phone"])

        for contact in contacts:
            writer.writerow([contact["name"], contact["phone"]])

    print("Contacts Exported Successfully")