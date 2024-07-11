import re
from colorama import Fore, Style


def phone_book_parse(user_input: str) -> tuple:
    pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = " ".join(parts[1:]).rsplit(" ", 1)
    if len(args) >= 2 and not re.match(pattern, args[-1]) and ("add" in cmd or "change" in cmd):
        print("wrong pattern of phone number")
    elif not re.match(pattern, args[-1]):
        args = (" ".join(args),)
    return cmd, *args


def add_contact(name: str, phone: str, contacts: dict):
    contacts[name] = phone
    print(f"Contact {name} added.")


def change_contact(name: str, phone: str, contacts: dict):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} updated")
    else:
        print("Contact is not found")


def show_phone(name: str, contacts: dict):
    if name in contacts:
        print(f"{name} - {contacts[name]}")
    else:
        print("Contact is not found")


def show_all(contacts: dict):
    if not contacts:
        print("No contacts available.")
    else:
        for key, value in contacts.items():
            print(f"{key}: {value}")


def delete_contact(name: str, contacts: dict):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted")
    else:
        print(f"{name} is not in your contact list")


def all_commands(commands_list: dict):
    for command in commands_list:
        print(f"{Fore.LIGHTBLUE_EX + Style.BRIGHT+command} - "
              f"{Fore.LIGHTGREEN_EX + Style.DIM + commands_list[command] 
                 + Style.RESET_ALL}")
