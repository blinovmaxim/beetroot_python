from rich.console import Console
from rich.prompt import Prompt
import json
import os.path
import uuid

print("Welcome to the Contacts v1.1!")

console = Console()
filename = "contacts.json"
contacts = []
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), filename)
with open(file_path, "r") as f:
    contacts = json.load(f)

    
menu = """
a - add a contact
d - remove the contact
p - print list of contacts
s - search for a contact
q - quit from app
"""
def process_action(action):
    if action == "q":
        print("Thank you! See you soon!")
        exit(0)
    elif action == "a":
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        phone = input("Enter a phone: ")
        address = input("Enter an address (optional): ")
        notes = input("Enter the notes (optional): ")
        
        def get_contacts():
            return contacts

        def add_contact(name, email, phone, address=None, notes=None):
            if name is None or email is None or phone is None:
                raise ValueError("Name, email and phone are required")

    address = address if len(address) > 0 else None
    notes = notes if len(notes) > 0 else None

    contact = {
        "id": str(uuid.uuid4()),
        "name": name, 
        "email": email, 
        "phone": phone, 
        "address": address, 
        "notes": notes
    }
    
    contacts = get_contacts()

    contacts.append(contact)

    with open(file_path, "w") as f:
        json.dump(contacts, f, indent=2)

        print("Contact added successfully!")

        add_contact(
            name, email, phone, address=address, notes=notes
        )

def main():
    while True:
        print(menu)

        action = Prompt.ask("Choise your action")

        process_action(action)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThank you. See you soon!")

