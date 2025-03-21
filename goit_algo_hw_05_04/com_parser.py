import re


def input_error(error_message):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return error_message
            except KeyError:
                return 'Name is not in contact list'
            except IndexError:
                return error_message
        return inner
    return decorator


def read_error(func):
    def inner(path):
        try:
            return func(path)
        except FileNotFoundError:
            with open('contacts_list.txt', 'w') as contacts_file:
                return contacts_file, 'Contacts file was not found, a new file has been created.'
    return inner


def phone_cleaner(func):
    def normalize_phone(args, contacts):
        phone = args.pop(1)
        if len(phone) >= 10:
            cleaned_num = re.sub(r'[^0-9]', '', phone)
            prepared_num = re.sub(r'^38|^8', '', cleaned_num)
            phone = '+38' + prepared_num
            args.insert(1, phone)
            return func(args, contacts)
        elif len(phone) > 13:
            return 'Phone number is to long, please check the phone number.'
        elif len(phone) < 10:
            return 'Phone number is to short, please check the phone number.'
    return normalize_phone


@input_error('Invalid command.')
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error("Enter the contact's name and phone number.")
@phone_cleaner
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return f'{name} is already in your contacts list.\nIf you want to change the phone number for {name}, use the command "change".'


@input_error("Enter the contact's name and phone number.")
@phone_cleaner
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Name not found in contact list."


@input_error("Enter the contact's name")
def contact_delete(args, contacts):
    name, = args
    contacts.pop(name)
    return f'{name} has been removed from your contact list.'
    

@input_error("Enter the contact's name")
def show_phone(args, contacts):
    name, = args
    return contacts[name]


def show_all(contacts):
    header = f"\n{'Contact name':<14} | {'Phone number'}\n" + "-" * 30
    main_text = '\n'.join(f'{item:<14} | {contacts[item]}' for item in contacts)
    result = header + "\n" + main_text + "\n"
    return result


def save_contacts(contacts_file, contacts):
    with open(contacts_file, 'w') as file:  
        file.write('\n'.join(f'{item};{contacts[item]}' for item in contacts))


@read_error
def read_contacts(contacts_file) -> dict:
    contacts = {}
    with open(contacts_file, 'r') as file:
        for line in file:
            name, phone = line.strip().split(';')
            contacts[name] = phone
    return contacts

