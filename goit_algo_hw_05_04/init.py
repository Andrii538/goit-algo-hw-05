from com_parser import read_contacts, read_error



def init():
    print("Welcome to the assistant bot!")
    commands = '''
    hello - для вітального повідомлення,
    help - для виклику цього повідомлення,
    close or exit - для припинення виконня бота,
    add - для додавання нового контакта, передається з імʼям і номером розділеними пробілом,
    phone - для показу номера телефона для конкретного контакта, передається з імʼям розділеними пробілом,
    delete - для видалення контакта, передається з імʼям розділеними пробілом,
    change - для зміни записаного номера для конкретного контакта, передається з імʼям і номером розділеними пробілом,
    all - для показу всіх збережених контактів з їх номерами.
    '''
    print(commands)
    contacts_file = 'contacts_list.txt'
    contacts = read_contacts(contacts_file)
    return contacts, contacts_file, commands