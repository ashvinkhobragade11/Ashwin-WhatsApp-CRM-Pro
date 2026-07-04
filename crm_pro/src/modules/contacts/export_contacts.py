import csv
from tkinter import filedialog, messagebox
from database import get_contacts

def export_contacts():

    contacts = get_contacts()

    if len(contacts) == 0:
        messagebox.showwarning(
            "No Data",
            "No Contacts Found."
        )
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[
            ("CSV Files", "*.csv")
        ],
        initialfile="contacts.csv"
    )

    if not file:
        return

    with open(
        file,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "ID",
            "Name",
            "Phone"
        ])

        for contact in contacts:
            writer.writerow(contact)

    messagebox.showinfo(
        "Success",
        "Contacts Exported Successfully."
    )