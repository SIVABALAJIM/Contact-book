# Contact Management System

contacts = {}

def add_contact():
    """Add a new contact."""
    name = input("Enter the contact's name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    address = input("Enter the address: ").strip()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

def view_contacts():
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    """Search for a contact."""
    query = input("Enter the name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if query == name or query == details["phone"]:
            print(f"\nFound Contact:\nName: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    """Update a contact's details."""
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    print(f"\nCurrent Details: {contacts[name]}")
    phone = input("Enter the new phone number (leave blank to keep current): ").strip()
    email = input("Enter the new email address (leave blank to keep current): ").strip()
    address = input("Enter the new address (leave blank to keep current): ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address
    print("Contact updated successfully!")

def delete_contact():
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def main():
    """Main menu for the Contact Management System."""
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the program
main()
