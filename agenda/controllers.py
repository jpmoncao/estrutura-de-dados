import sqlite3

DB_TABLE = 'contacts'

def main():
    return 0

def connect_db():
    conn = sqlite3.connect(__file__ + "/../agenda.db")
    conn.row_factory = sqlite3.Row 
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE IF NOT EXISTS {DB_TABLE}(id_contact INTEGER PRIMARY KEY, name TEXT, tel TEXT)")
    return conn, cur

def autoincrement_contacts():
    conn, cur = connect_db()
    sql = f"SELECT MAX(id_contact) FROM {DB_TABLE}"
    res = cur.execute(sql)
    contact = res.fetchone()[0]
    cur.close()
    conn.close()

    if not contact:
        contact = 0

    return contact + 1

def select_contacts(order='', is_desc=False):
    conn, cur = connect_db()
    sql = f"SELECT * FROM {DB_TABLE}"
    if order.strip() != '':
        sql = f"SELECT * FROM {DB_TABLE} ORDER BY {order} {'DESC' if is_desc else 'ASC'}"
    res = cur.execute(sql)
    contacts = [dict(contact) for contact in res.fetchall()] 
    cur.close()
    conn.close()

    return contacts

def select_contact(id_contact):
    conn, cur = connect_db()
    sql = f"SELECT * FROM {DB_TABLE} WHERE id_contact = {id_contact}"
    cur.execute(sql)
    contact = cur.fetchone()
    cur.close()
    conn.close()

    if contact:
        return dict(contact) 

    return contact

def insert_contact(contact):
    conn, cur = connect_db()
    sql = f"INSERT INTO {DB_TABLE} (id_contact, name, tel) VALUES (?, ?, ?)"
    cur.execute(sql, (contact['id_contact'], contact['name'], contact['tel']))
    conn.commit()
    cur.close()
    conn.close()
    return contact

def update_contact(contact):
    conn, cur = connect_db()
    sql = f"UPDATE {DB_TABLE} SET name = ?, tel = ? WHERE id_contact = ?"
    cur.execute(sql, (contact['name'], contact['tel'], contact['id_contact']))
    conn.commit()
    cur.close()
    conn.close()

def delete_contact(id_contact):
    if not select_contact(id_contact):
        return False

    conn, cur = connect_db()
    sql = f"DELETE FROM {DB_TABLE} WHERE id_contact = ?"
    cur.execute(sql, (id_contact,))
    conn.commit()
    cur.close()
    conn.close()

    return True

if __name__ == '__main__':
    main()