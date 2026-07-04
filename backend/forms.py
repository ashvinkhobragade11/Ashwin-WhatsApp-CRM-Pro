import tkinter as tk
from tkinter import messagebox
from backend.database import load_contacts, save_contacts

def open_add_contact():

    window = tk.Toplevel()
    window.title("Add Contact")
    window.geometry("350x250")
    window.resizable(False, False)

    tk.Label(window, text="Name", font=("Arial",12)).pack(pady=5)
    name_entry=tk.Entry(window,width=30)
    name_entry.pack()

    tk.Label(window,text="Phone",font=("Arial",12)).pack(pady=5)
    phone_entry=tk.Entry(window,width=30)
    phone_entry.pack()

    def save():

        contacts=load_contacts()

        contacts.append({
            "name":name_entry.get(),
            "phone":phone_entry.get()
        })

        save_contacts(contacts)

        messagebox.showinfo("Success","Contact Added Successfully")

        window.destroy()

    tk.Button(
        window,
        text="Save Contact",
        bg="green",
        fg="white",
        width=20,
        command=save
    ).pack(pady=20)


def open_search_contact():

    window=tk.Toplevel()

    window.title("Search Contact")

    window.geometry("350x250")

    tk.Label(window,text="Phone Number",font=("Arial",12)).pack(pady=10)

    phone_entry=tk.Entry(window,width=30)

    phone_entry.pack()

    result=tk.Label(window,text="",font=("Arial",12))

    result.pack(pady=20)

    def search():

        contacts=load_contacts()

        phone=phone_entry.get()

        for contact in contacts:

            if contact["phone"]==phone:

                result.config(
                    text=f'Name : {contact["name"]}\nPhone : {contact["phone"]}',
                    fg="green"
                )

                return

        result.config(
            text="Contact Not Found",
            fg="red"
        )

    tk.Button(
        window,
        text="Search",
        bg="blue",
        fg="white",
        width=20,
        command=search
    ).pack(pady=10)