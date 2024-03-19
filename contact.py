import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.master.geometry("1000x1000")
        self.master.configure(bg="#FFFFFF")  # White background color

        self.contacts = []

        self.home_page()

    def home_page(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Contact Book", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=50)

        add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact, font=("Helvetica", 16))
        add_button.pack(pady=10)

        view_button = tk.Button(self.master, text="View Contact List", command=self.view_contacts, font=("Helvetica", 16))
        view_button.pack(pady=10)

        search_button = tk.Button(self.master, text="Search Contact", command=self.search_contact, font=("Helvetica", 16))
        search_button.pack(pady=10)

        update_button = tk.Button(self.master, text="Update Contact", command=self.update_contact, font=("Helvetica", 16))
        update_button.pack(pady=10)

        delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact, font=("Helvetica", 16))
        delete_button.pack(pady=10)

    def add_contact(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Add Contact", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=50)

        name_label = tk.Label(self.master, text="Name:", font=("Helvetica", 16), bg="#FFFFFF")
        name_label.pack()

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.name_entry.pack()

        phone_label = tk.Label(self.master, text="Phone:", font=("Helvetica", 16), bg="#FFFFFF")
        phone_label.pack()

        self.phone_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.phone_entry.pack()

        email_label = tk.Label(self.master, text="Email:", font=("Helvetica", 16), bg="#FFFFFF")
        email_label.pack()

        self.email_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.email_entry.pack()

        address_label = tk.Label(self.master, text="Address:", font=("Helvetica", 16), bg="#FFFFFF")
        address_label.pack()

        self.address_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.address_entry.pack()

        save_button = tk.Button(self.master, text="Save", command=self.save_contact, font=("Helvetica", 16))
        save_button.pack(pady=20)

        back_button = tk.Button(self.master, text="Back", command=self.home_page, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def save_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Warning", "Name and Phone fields are required.")
            return

        if not phone.isdigit():
            messagebox.showwarning("Warning", "Phone number should contain numbers only.")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        self.contacts.append(contact)
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def view_contacts(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Contact List", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        if self.contacts:
            for contact in self.contacts:
                info = f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n"
                contact_label = tk.Label(self.master, text=info, font=("Helvetica", 16), bg="#FFFFFF")
                contact_label.pack(anchor="w", pady=10)
        else:
            label = tk.Label(self.master, text="No contacts found.", font=("Helvetica", 16), bg="#FFFFFF")
            label.pack(pady=20)

        back_button = tk.Button(self.master, text="Back", command=self.home_page, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def search_contact(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Search Contact", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        search_entry = tk.Entry(self.master, font=("Helvetica", 16))
        search_entry.pack(pady=10)

        search_button = tk.Button(self.master, text="Search", command=lambda: self.display_search_result(search_entry.get()), font=("Helvetica", 16))
        search_button.pack(pady=10)

        back_button = tk.Button(self.master, text="Back", command=self.home_page, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def display_search_result(self, keyword):
        self.clear_screen()

        label = tk.Label(self.master, text=f"Search Results for '{keyword}'", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        found = False
        for contact in self.contacts:
            if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
                info = f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n"
                contact_label = tk.Label(self.master, text=info, font=("Helvetica", 16), bg="#FFFFFF")
                contact_label.pack(anchor="w", pady=10)
                found = True

        if not found:
            label = tk.Label(self.master, text="No contacts found.", font=("Helvetica", 16), bg="#FFFFFF")
            label.pack(pady=20)

        back_button = tk.Button(self.master, text="Back", command=self.search_contact, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def update_contact(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Update Contact", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        search_entry = tk.Entry(self.master, font=("Helvetica", 16))
        search_entry.pack(pady=10)

        search_button = tk.Button(self.master, text="Search", command=lambda: self.display_update_contact(search_entry.get()), font=("Helvetica", 16))
        search_button.pack(pady=10)

        back_button = tk.Button(self.master, text="Back", command=self.home_page, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def display_update_contact(self, keyword):
        self.clear_screen()

        label = tk.Label(self.master, text=f"Update Contact for '{keyword}'", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        found = False
        for contact in self.contacts:
            if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
                found = True
                self.show_update_form(contact)
                break

        if not found:
            label = tk.Label(self.master, text="Contact not found.", font=("Helvetica", 16), bg="#FFFFFF")
            label.pack(pady=20)

        back_button = tk.Button(self.master, text="Back", command=self.update_contact, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def show_update_form(self, contact):
        name_label = tk.Label(self.master, text="Name:", font=("Helvetica", 16), bg="#FFFFFF")
        name_label.pack()

        self.name_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.name_entry.insert(0, contact['Name'])
        self.name_entry.pack()

        phone_label = tk.Label(self.master, text="Phone:", font=("Helvetica", 16), bg="#FFFFFF")
        phone_label.pack()

        self.phone_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.phone_entry.insert(0, contact['Phone'])
        self.phone_entry.pack()

        email_label = tk.Label(self.master, text="Email:", font=("Helvetica", 16), bg="#FFFFFF")
        email_label.pack()

        self.email_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.email_entry.insert(0, contact['Email'])
        self.email_entry.pack()

        address_label = tk.Label(self.master, text="Address:", font=("Helvetica", 16), bg="#FFFFFF")
        address_label.pack()

        self.address_entry = tk.Entry(self.master, font=("Helvetica", 16))
        self.address_entry.insert(0, contact['Address'])
        self.address_entry.pack()

        save_button = tk.Button(self.master, text="Save", command=lambda: self.save_updated_contact(contact), font=("Helvetica", 16))
        save_button.pack(pady=20)

    def save_updated_contact(self, old_contact):
        new_name = self.name_entry.get().strip()
        new_phone = self.phone_entry.get().strip()
        new_email = self.email_entry.get().strip()
        new_address = self.address_entry.get().strip()

        if not new_name or not new_phone:
            messagebox.showwarning("Warning", "Name and Phone fields are required.")
            return

        if not new_phone.isdigit():
            messagebox.showwarning("Warning", "Phone number should contain numbers only.")
            return

        for contact in self.contacts:
            if contact == old_contact:
                contact['Name'] = new_name
                contact['Phone'] = new_phone
                contact['Email'] = new_email
                contact['Address'] = new_address
                break

        messagebox.showinfo("Success", "Contact updated successfully!")
        self.clear_entries()

    def delete_contact(self):
        self.clear_screen()

        label = tk.Label(self.master, text="Delete Contact", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        search_entry = tk.Entry(self.master, font=("Helvetica", 16))
        search_entry.pack(pady=10)

        search_button = tk.Button(self.master, text="Search", command=lambda: self.display_delete_contact(search_entry.get()), font=("Helvetica", 16))
        search_button.pack(pady=10)

        back_button = tk.Button(self.master, text="Back", command=self.home_page, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def display_delete_contact(self, keyword):
        self.clear_screen()

        label = tk.Label(self.master, text=f"Delete Contact for '{keyword}'", font=("Helvetica", 24), bg="#FFFFFF")
        label.pack(pady=20)

        found = False
        for contact in self.contacts:
            if keyword.lower() in contact['Name'].lower() or keyword in contact['Phone']:
                found = True
                info = f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n"
                contact_label = tk.Label(self.master, text=info, font=("Helvetica", 16), bg="#FFFFFF")
                contact_label.pack(anchor="w", pady=10)

                delete_button = tk.Button(self.master, text="Delete", command=lambda: self.remove_contact(contact), font=("Helvetica", 16))
                delete_button.pack(pady=20)
                break

        if not found:
            label = tk.Label(self.master, text="Contact not found.", font=("Helvetica", 16), bg="#FFFFFF")
            label.pack(pady=20)

        back_button = tk.Button(self.master, text="Back", command=self.delete_contact, font=("Helvetica", 16))
        back_button.pack(pady=10)

    def remove_contact(self, contact):
        self.contacts.remove(contact)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        self.delete_contact()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.configure(bg="#ADD8E6")  # Blue background color
    app = ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
