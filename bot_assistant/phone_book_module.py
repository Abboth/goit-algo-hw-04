import re
from colorama import Fore, Style, init

init(autoreset=True)


def phone_book_parse(user_input: str):
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
    return f"Contact {name} added."


def change_contact(name: str, phone: str, contacts: dict):
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated"
    else:
        return "Contact is not found"


def show_phone(name: str, contacts: dict):
    if name in contacts:
        return f"{name} - {contacts[name]}"
    else:
        return "Contact is not found"


def show_all(contacts: dict):
    if not contacts:
        return "No contacts available."
    else:
        for key, value in contacts.items():
            return f"{key}: {value}"


def delete_contact(name: str, contacts: dict):
    if name in contacts:
        del contacts[name]
        return f"Contact {name} deleted"
    else:
        return f"{name} is not in your contact list"


def all_commands(commands_list: dict):
    # "".join(commands_list)+"\n"
    # for command in commands_list:
    #     commands += (f"{Fore.LIGHTBLUE_EX + Style.BRIGHT+command} - "
    #                  f"{Fore.LIGHTGREEN_EX + Style.DIM + commands_list[command]}\n")
    return "".join(commands_list)+"\n"
