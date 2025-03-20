from com_parser import *
from init import init


def main():
    """
    Консольний бот-помічник, який розпізнає команди, що вводяться з клавіатури, та відповідає згідно із введеною командою.
    Він вміє зберігати, змінювати, видаляти та показувати збережені контакти і відповідні номери телефонів.
    """
    contacts, contacts_file, commands = init()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            save_contacts(contacts_file, contacts)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'delete':
            print(contact_delete(args, contacts))
        elif command == 'help':
            print(commands)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    init()
    main()
