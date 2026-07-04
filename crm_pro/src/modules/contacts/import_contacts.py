import csv
from tkinter import filedialog, messagebox

from database import add_contact


def import_contacts():

    file = filedialog.askopenfilename(
        filetypes=[
            ("CSV Files", "*.csv")
        ]
    )

    if not file:
        return

    with open(
        file,
        "r",
        encoding="utf-8"
    ) as csvfile:

        reader = csv.reader(csvfile)

        next(reader)

        count = 0

        for row in reader:

            if len(row) < 3:
                continue

            name = row[1].strip()
            phone = row[2].strip()

            add_contact(
                name,
                phone
            )

            count += 1

    messagebox.showinfo(
        "Success",
        f"{count} Contacts Imported Successfully."
    )