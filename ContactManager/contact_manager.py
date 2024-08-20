import pickle

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def save_contacts(self):
        with open('contacts.pkl', 'wb') as f:
            pickle.dump(self.contacts, f)

    def load_contacts(self):
        try:
            with open('contacts.pkl', 'rb') as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts 
                   if search_term in contact.name or search_term in contact.phone]
        for contact in results:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")

    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name == name:
                if phone:
                    contact.phone = phone
                if email:
                    contact.email = email
                if address:
                    contact.address = address
                self.save_contacts()
                return
        print("Contact not found.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

def user_interface():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, phone if phone else None, email if email else None, address if address else None)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            manager.delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interface()
