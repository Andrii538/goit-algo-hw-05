from com_parser import read_contacts


def init():
    print("Welcome to the assistant bot!")
    commands = '''
    hello - для вітального повідомлення,
    help - для виклику цього повідомлення,
    close or exit - для припинення виконання бота,
    add - для додавання нового контакту, передається з імʼям і номером розділеними пробілом,
    phone - для показу номера телефону для конкретного контакту, передається з імʼям розділеними пробілом,
    delete - для видалення контакту, передається з імʼям розділеними пробілом,
    change - для зміни записаного номера для конкретного контакту, передається з імʼям і номером розділеними пробілом,
    all - для показу всіх збережених контактів з їх номерами.
    joke - для показу випадкового жарту.
    '''
    print(commands)
    contacts_file = 'contacts_list.txt'
    contacts = read_contacts(contacts_file)
    return contacts, contacts_file, commands
