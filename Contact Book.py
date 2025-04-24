class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact}")

    def search_contact(self, name):
        results = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if results:
            print("Search Results:")
            for contact in results:
                print(contact)
        else:
            print(f"No contacts found for '{name}'.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                removed_contact = self.contacts.pop(i)
                print(f"Contact '{removed_contact.name}' deleted.")
                return
        print(f"No contact found with the name '{name}'.")


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
