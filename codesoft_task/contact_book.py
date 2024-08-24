def get_contact_input():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return name, phone, email, address

def add_contact(contacts):
    name, phone, email, address = get_contact_input()
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact added successfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["phone"]:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Enter new details (leave blank to keep current value):")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

