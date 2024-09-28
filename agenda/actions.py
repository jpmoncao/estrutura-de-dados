import controllers

def main():
    return 0

def insert():
    id_contact = controllers.autoincrement_contacts()

    while True:
        name = str(input('Nome: '))
        if name.strip() == '':
            continue
        break
    while True:
        tel = str(input('Telefone: '))
        if len(tel.strip()) < 9:
            continue
        break

    contact = {
        'id_contact': id_contact,
        'name': name,
        'tel': tel,
    }

    controllers.insert_contact(contact)

    print(f'\033[1m------------------------------------------------\033[m')
    print(f'\033[1m|  ID | Nome                 | Telefone        | \033[m')
    print(f'\033[1m|\033[m \033[3m{contact['id_contact']:3}\033[m \033[1m|\033[m {contact['name']:20} \033[1m|\033[m {contact['tel']:15} \033[1m|\033[m')
    print(f'\033[1m------------------------------------------------\033[m')

def list_all():
    contacts = controllers.select_contacts()

    if len(contacts) == 0:
        print('\033[1mAgenda vazia!\033[m')
        return

    print(f'\033[1m------------------------------------------------\033[m')
    print(f'\033[1m|  ID | Nome                 | Telefone        | \033[m')

    for contact in contacts:
        print(f'\033[1m|\033[m \033[3m{contact['id_contact']:3}\033[m \033[1m|\033[m {contact['name']:20} \033[1m|\033[m {contact['tel']:15} \033[1m|\033[m')
    print(f'\033[1m------------------------------------------------\033[m')

def list_contact():
    id_contact = int(input('\033[1mCódigo: \033[m'))

    contact = controllers.select_contact(id_contact)

    if contact['id_contact'] == 0:
        print('\033[1mContato não encontrado!\033[m')
        return
    
    print(f'\033[1m------------------------------------------------\033[m')
    print(f'\033[1m|  ID | Nome                 | Telefone        | \033[m')
    print(f'\033[1m|\033[m \033[3m{contact['id_contact']:3}\033[m \033[1m|\033[m {contact['name']:20} \033[1m|\033[m {contact['tel']:15} \033[1m|\033[m')
    print(f'\033[1m------------------------------------------------\033[m')

def edit():
    id_contact = int(input('\033[1mCódigo: \033[m'))

    contact = controllers.select_contact(id_contact)

    if contact['id_contact'] == 0:
        print('\033[1mContato não encontrado!\033[m')
        return
    
    while True:
        name = str(input(f'Nome \033[3m({contact['name']})\033[m: '))
        if name.strip() == '':
            name = contact['name']
        break
    while True:
        tel = str(input(f'Telefone \033[3m({contact['tel']})\033[m: '))
        if tel.strip() == '':
            tel = contact['tel']
        if len(tel.strip()) < 9:
            continue
        break

    contact['name'] = name
    contact['tel'] = tel     
    
    print(f'\033[1m------------------------------------------------\033[m')
    print(f'\033[1m|  ID | Nome                 | Telefone        | \033[m')
    print(f'\033[1m|\033[m \033[3m{contact['id_contact']:3}\033[m \033[1m|\033[m {contact['name']:20} \033[1m|\033[m {contact['tel']:15} \033[1m|\033[m')
    print(f'\033[1m------------------------------------------------\033[m')   

def orderby_name():
    contacts = controllers.select_contacts()

    if len(contacts) == 0:
        print('\033[1mAgenda vazia!\033[m')
        return

    def ordem(contact):
        return contact['name'].lower()

    contacts.sort(key=ordem)

    print(f'\033[1m------------------------------------------------\033[m')
    print(f'\033[1m|  ID | Nome                 | Telefone        | \033[m')

    for contact in contacts:
        print(f'\033[1m|\033[m \033[3m{contact['id_contact']:3}\033[m \033[1m|\033[m {contact['name']:20} \033[1m|\033[m {contact['tel']:15} \033[1m|\033[m')
    print(f'\033[1m------------------------------------------------\033[m')
    

if __name__ == '__main__':
    main()