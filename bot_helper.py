import re

from bot_assistant import phone_book_module
from colorama import Fore, Style


def main():
    contacts = {}
    commands_list = {"back": "to back to previous menu",
                     "all": "to show all contact list",
                     "show 'contact name'": "to show contact phone number",
                     "delete 'contact name'": "to delete contact",
                     "commands": "to show all available commands",
                     "add 'contact name' 'phone number'": "to add contact number",
                     "change 'contact name' 'contact number'": "to editing exists contact"
                     }
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("What do you want to edit?\nPhone book\nCalendar\nExit to quit\n")

        if user_input in ["close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif user_input == "phone book":

            while True:
                phone_book_input = input(f"Enter a command, or type (Back) to move in previous menu : ").lower()
                command, *args = phone_book_module.phone_book_parse(phone_book_input)
                invalid_command = \
                    (f"{Fore.RED + Style.BRIGHT} invalid command format! type 'Commands' to see command list "
                     f"{Style.RESET_ALL}")
                if len(args) <= 1:
                    name = args[0]
                    if command == "back":
                        break
                    elif command == "all":
                        phone_book_module.show_all(contacts)
                    elif command == "show":
                        phone_book_module.show_phone(name, contacts)
                    elif command == "delete":
                        phone_book_module.delete_contact(name, contacts)
                    elif command == "commands":
                        phone_book_module.all_commands(commands_list)
                    else:
                        print(f"{invalid_command}")

                elif len(args) >= 2:
                    name, phone = args
                    pattern = r"^\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
                    if re.match(pattern, phone):
                        if command == "add":
                            phone_book_module.add_contact(name, phone, contacts)
                        elif command == "change":
                            phone_book_module.change_contact(name, phone, contacts)
                else:
                    print(f"{invalid_command}")
        elif user_input == "calendar":
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "still in developing" + Style.RESET_ALL)
        else:
            print("invalid command.")


if __name__ == "__main__":
    main()
