from menu import show_menu, meeting
from actions import insert, list_all, list_contact, edit, orderby_name

meeting()

while True:
    option_selected = show_menu()

    if option_selected == 1:
        insert()
    elif option_selected == 2:
        list_all()
    elif option_selected == 3:
        list_contact()
    elif option_selected == 4:
        edit()
    elif option_selected == 5:
        orderby_name()
    elif option_selected == 7:
        break
