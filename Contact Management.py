import re

def validate_input(pattern, prompt):
    while True:
        data = input(prompt)
        if re.fullmatch(pattern, data):
            return data
        else:
            print("Invalid input format. Please try again.")


def read_contacts(filename='Contact_List.txt'):   
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.strip():  
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        email, name, phone, additional_info = parts
                        print(f"Email: {email}")
                        print(f"Name: {name}")
                        print(f"Phone: {phone}")
                        print(f"Additional Info: {additional_info}")
                        print("---------")
        print(f"Contacts read successfully from {filename}.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred while reading contacts: {e}")

    
def add_contacts(contacts, filename="Contact_List.txt"):
    email = validate_input(r'[^@]+@[^@]+\.[^@]+', "Enter email address: ")
    if email in contacts:
        print("Contact with this unique identifier already exists.")
        return
    name = input("Enter name: ")
    phone = validate_input(r'\d{10}', "Enter phone number (10 digits): ")
    additional_info = input("Enter additional information (address, notes): ")
    
    contacts[email] = {
        'Name': name,
        'Phone': phone,
        'Additional Info': additional_info
    }
    print("Contact added successfully.")

    try:
        with open(filename, 'a') as file:
            file.write(f"\n{email}:{name},{phone},{additional_info}\n")
        print(f"Contact saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving the contact: {e}")

def edit_contacts(contacts, filename= 'Contact_List.txt'):
    old_email = validate_input(r'[^@]+@[^@]+\.[^@]+', "Enter email address of the contact to edit: ")
    if old_email not in contacts:
        print("Contact not found.")
        return
    else:
        print("Leave the field blank if you don't want to change it.")
        new_email = validate_input(r'[^@]+@[^@]+\.[^@]+', "Enter new email address of the contact to edit: ")
        name = input("Enter name: ") or contacts[old_email]['Name']
        phone = input("Enter phone number (10 digits): ")or contacts[old_email]['Phone']
    
        additional_info = input("Enter additional information (address, notes): ")or contacts[old_email]['Additional Info']

    if new_email != old_email and new_email in contacts:
        print("Contact with this new email already exists.")

    if new_email != old_email:
        del contacts[old_email]

    contacts[new_email] = {
        'Name': name,
        'Phone': phone,
        'Additional Info': additional_info
    }
    
   
    print("Contact edited successfully.")
    export_contacts(contacts, filename)

def delete_contacts(contacts, filename='Contact_List.txt'):
    email = validate_input(r'[^@]+@[^@]+\.[^@]+', "Enter email address of the contact to delete: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully.")
        export_contacts(contacts, filename)
    else:
        print("Contact not found.")

def search_for_contacts(contacts):
    email = validate_input(r'\S+', "Enter unique identifier of the contact to search: ")
    if email in contacts:
        contact = contacts[email]
        
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Additional Info: {contact['Additional Info']}")
    else:
        print("Contact not found.")

def export_contacts(contacts, filename="Contact_List.txt"):
    try:
        with open(filename, 'w') as file:
            for email, contact in contacts.items():
                file.write(f"{email},{contact['Name']},{contact['Phone']},{contact['Additional Info']}\n")
        print("Contacts exported successfully.")
    except Exception as e:
        print(f"An error occurred while exporting contacts: {e}")

def display_contacts(contacts):
    if contacts:
        for email, contact in contacts.items():
            print(f"Email: {email}")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Additional Info: {contact['Additional Info']}")
            print("---------")
    else:
        print("No contacts available.")

def main():
    contacts = {}
    while True:
        print("\nWelcome to the Contact Management Application!\n")
        print("Menu: ")
        print("1. Add Contact")
        print("2. Edit Existing Contact")
        print("3. Delete a Contact")
        print("4. Search for Contact")
        print("5. Export Contacts to file")
        print("6. Display all Contacts")
        print("7. Read Contacts")
        print("8. Exit")

        selection = input("Please enter your option (1-8): ")
        if selection == "1":
            add_contacts(contacts)
            #write_contacts('Contact_List.txt', contacts)
        elif selection == "2":
            edit_contacts(contacts)
        elif selection == "3":
            delete_contacts(contacts)
        elif selection == "4":
            search_for_contacts(contacts)
        elif selection == "5":
            export_contacts(contacts)
        elif selection == "6":
            display_contacts(contacts)
        elif selection == "7":
            read_contacts()
        elif selection == "8":
            print("\nExiting the Contact Management System. Goodbye!\n")
            break
        else:
            print("Please enter a valid selection.")

main()