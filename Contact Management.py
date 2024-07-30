import re


with open('Contact_List.txt', 'w') as file:
    file.write("Contact List Elements:")

def validate_input(pattern, prompt):
    while True:
        data = input(prompt)
        if re.fullmatch(pattern, data):
            return data
        else:
            print("Invalid input format. Please try again.")


def read_contacts(filename, contacts):
    try:
        with open(filename, 'r') as file:
            contacts = []
            for line in file:
                name, phone_number, email_address, additional_info = line.strip().split(',')
                contacts.append({'name': name, 'phone_number': phone_number, 'email_address': email_address, 'additonal info': additional_info.split(',')})
                return contacts
    except FileNotFoundError:
        []

#def write_contacts(filename, contacts):
 #   with open(filename, 'a') as file:
  #      for contact in contacts:
   #         file.write(f"{contacts[name]}, {contacts[phone_number]}, {contacts[email_address]}, {contacts[additional_info]}\n")

def add_contacts(contacts):
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
def edit_contacts(contacts):
    pass
def delete_contacts(contacts):
    pass
def search_for_contacts(contacts):
    pass
def export_contacts(contacts):
    pass
def display_contacts(contacts):
    pass



def main():
    contacts = read_contacts('Contact_List.txt')

    while True:
        print("Welcome to the Contact Management Application!")
        print("Menu: ")
        print("1. Add Contact")
        print("2. Edit Existing Contact")
        print("3. Delete a Contact")
        print("4. Search for Contact")
        print("5. Display all Contacts")
        print("6. Export Contacts to file")
        print("7. Exit")

        selection = input("Please enter your option (1-7): ")
        if selection == "1":
            add_contacts()
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
            break
        else:
            print("Please enter a valid selection.")
