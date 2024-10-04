import controllers
from menu import table, show_orders
from utils import bold, error, warn

def main():
    return 0

def insert():
    id_contact = controllers.autoincrement_contacts()

    while True:
        name = str(input('Nome: '))
        if name.strip() == '':
            error('Nome inválido/não informado!')
            continue
        break
    while True:
        tel = str(input('Telefone: '))
        if len(tel.strip()) < 9:
            error('Telefone inválido/não informado!')
            continue
        break

    contact = {
        'id_contact': id_contact,
        'name': name,
        'tel': tel,
    }

    controllers.insert_contact(contact)

    table([contact])

def list_all():
    contacts = controllers.select_contacts()

    if len(contacts) == 0:
        warn('Agenda vazia!')
        return

    table(contacts)

def list_contact():
    id_contact = int(input('\033[1mCódigo: \033[m'))

    contact = controllers.select_contact(id_contact)

    if not contact:
        warn('Contato não encontrado!')
        return
    
    table([contact])

def edit():
    id_contact = int(input('\033[1mCódigo: \033[m'))

    contact = controllers.select_contact(id_contact)

    if not contact:
        warn('Contato não encontrado!')
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
            error('Telefone inválido/não informado!')
            continue
        break

    contact['name'] = name
    contact['tel'] = tel     

    controllers.update_contact(contact)
    
    table([contact])

def orderby():
    order = show_orders()
    if order == 7:
        print()
        return

    if order in [2,4,6]:
        is_desc = True
        if order == 2:
            key = 'id_contact'
        elif order == 4:
            key = 'name'
        elif order == 4:
            key = 'tel'
    elif order in [1,3,5]:
        is_desc = False
        if order == 1:
            key = 'id_contact'
        elif order == 3:
            key = 'name'
        elif order == 5:
            key = 'tel'

    contacts = controllers.select_contacts(key, is_desc)

    if len(contacts) == 0:
        warn('Agenda vazia!')
        return

    table(contacts)
    
def delete():
    id_contact = int(input('\033[1mCódigo: \033[m'))

    contact = controllers.select_contact(id_contact)

    if not contact:
        warn('Contato não encontrado!')
        return
    
    if controllers.delete_contact(contact['id_contact']):
        bold('Conta apagada com sucesso!')

def save_file():
    contacts = controllers.select_contacts()

    if len(contacts) == 0:
        warn('Agenda vazia!')
        return
    
    lines = []
    lines.append('-'*48)
    lines.append('\n' + '|  ID | Nome                 | Telefone        | ')
    for contact in contacts:
        lines.append('\n' + f'| {contact['id_contact']:3} | {contact['name']:20} | {contact['tel']:15} |')
    lines.append('\n' + '-'*48)

    with open(__file__+'/../agenda.txt', 'w', -1, 'utf-8') as arquivo:
        arquivo.writelines(lines)

    bold('Arquivo criado com sucesso! "' + __file__ +'\\..\\agenda.txt" \n')

if __name__ == '__main__':
    main()