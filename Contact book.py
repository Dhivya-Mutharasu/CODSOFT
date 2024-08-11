import json

def load_con():
    """Loads contacts from a JSON file."""
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_con(contacts):
    """Saves contacts to a JSON file."""
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_con(contacts):
    """Adds a new contact to the contact list."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    save_con(contacts)
    print("Contact added successfully!")

def view_con(contacts):
    """Displays all saved contacts."""
    if not contacts:
        print("No contacts found.")
        return
    print("\nContacts:")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print("-" * 20)

def search_con(contacts):
    """Searches for a contact by name or phone number."""
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print("-" * 20)
            found = True
    if not found:
        print("Contact not found.")

def update_con(contacts):
    """Updates the details of an existing contact."""
    name = input("Enter name of contact to update: ")
    if name in contacts:
        print("Current details:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        update_choice = input("What would you like to update? (phone/email/address/all/cancel): ")
        if update_choice.lower() == 'phone':
            contacts[name]['phone'] = input("Enter new phone number: ")
        elif update_choice.lower() == 'email':
            contacts[name]['email'] = input("Enter new email address: ")
        elif update_choice.lower() == 'address':
            contacts[name]['address'] = input("Enter new address: ")
        elif update_choice.lower() == 'all':
            contacts[name]['phone'] = input("Enter new phone number: ")
            contacts[name]['email'] = input("Enter new email address: ")
            contacts[name]['address'] = input("Enter new address: ")
        elif update_choice.lower() == 'cancel':
            print("Update cancelled.")
            return
        else:
            print("Invalid choice.")
            return
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_con(contacts):
    """Deletes a contact from the list."""
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        save_con(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    """Main function for the contact management program."""
    contacts = load_con()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_con(contacts)
        elif choice == '2':
            view_con(contacts)
        elif choice == '3':
            search_con(contacts)
        elif choice == '4':
            update_con(contacts)
        elif choice == '5':
            delete_con(contacts)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
