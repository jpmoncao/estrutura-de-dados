contacts = [
    {
        'id_contact': 1,
        'name': 'João Pedro',
        'tel': '(17)988116153'
    },
    {
        'id_contact': 2,
        'name': 'aaaaaaJoão Pedro',
        'tel': '(17)988116153'
    },
]

def main():
    return 0

def autoincrement_contacts():
    contacts = select_contacts()

    contacts_id = [contact['id_contact'] for contact in contacts]

    return max(contacts_id) + 1

def select_contacts():
    return contacts

def select_contact(id_contact):
    for contact in contacts:
        if contact['id_contact'] == id_contact:
            return contact
    return {
        'id_contact': 0
    }
    

def insert_contact(contact):
    contacts.append(contact)

    return contact
        

if __name__ == '__main__':
    main()