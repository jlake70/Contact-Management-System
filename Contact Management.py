import re


#with open('Contact_List.txt', 'w') as file:
    #file.write("Contact List Elements:")

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
            contacts = {}
            for line in file:
                identifier, name, phone_number, email_address, additional_info = line.strip().split(',')
                contacts.append({'unique id': identifier.split(':'),'Name': name, 'Phone': phone_number, 'Email': email_address, 'Additonal Info': additional_info.split(',')})
                return contacts
    except FileNotFoundError:
        []
    except Exception as e:
        print(f"An error occurred while reading Contact_List: {e}")

#def write_contacts(filename, contacts):
 #   with open(filename, 'a') as file:
  #      for contact in contacts:
   #         file.write(f"{contacts[name]}, {contacts[phone_number]}, {contacts[email_address]}, {contacts[additional_info]}\n")

def add_contacts(contacts, filename="Contact_List.txt"):
    unique_id = validate_input(r'\S+', "Enter unique identifier (e.g., phone number, email): ")
    if unique_id in contacts:
        print("Contact with this unique identifier already exists.")
        return
    name = input("Enter name: ")
    phone = validate_input(r'\d{10}', "Enter phone number (10 digits): ")
    email = validate_input(r'[^@]+@[^@]+\.[^@]+', "Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")
    
    contacts[unique_id] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact added successfully.")

    try:
        with open(filename, 'a') as file:
            file.write(f"\n{unique_id.split(':')},{name},{phone},{email},{additional_info}\n")
        print(f"Contact saved to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while saving the contact: {e}")
def edit_contacts(contacts):
    unique_id = validate_input(r'\S+', "Enter unique identifier of the contact to edit: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return
    print("Leave the field blank if you don't want to change it.")
    name = input("Enter name: ")
    phone = input("Enter phone number (10 digits): ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")

    if name:
        contacts[unique_id]['Name'] = name
    if phone:
        if re.fullmatch(r'\d{10}', phone):
            contacts[unique_id]['Phone'] = phone
        else:
            print("Invalid phone number format.")
    if email:
        if re.fullmatch(r'[^@]+@[^@]+\.[^@]+', email):
            contacts[unique_id]['Email'] = email
        else:
            print("Invalid email format.")
    if additional_info:
        contacts[unique_id]['Additional Info'] = additional_info
    
    print("Contact edited successfully.")
def delete_contacts(contacts):
    unique_id = validate_input(r'\S+', "Enter unique identifier of the contact to delete: ")
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_for_contacts(contacts):
    unique_id = validate_input(r'\S+', "Enter unique identifier of the contact to search: ")
    if unique_id in contacts:
        contact = contacts[unique_id]
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Additional Info: {contact['Additional Info']}")
    else:
        print("Contact not found.")
def export_contacts(contacts, filename="Contact_List.txt"):
    with open(filename, 'w') as file:
        for unique_id, contact in contacts.items():
            file.write(f"{unique_id},{contact['Name']},{contact['Phone']},{contact['Email']},{contact['Additional Info']}\n")
    print("Contacts exported successfully.")
def display_contacts(contacts):
    if contacts:
        for unique_id, contact in contacts.items():
            print(f"Identifier: {unique_id}")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
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
        print("5. Display all Contacts")
        print("6. Export Contacts to file")
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