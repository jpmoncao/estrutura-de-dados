def show_menu():
    while True:
        print_menu()
        option = int(input('\033[1m'))
        print('\033[m', end='')
        if option in range(1,8):
            return option

def print_menu():
    print(
'''\033[1;34m======================== MENU =========================\033[m
\033[1;34m1)\033[m Inserir contato
\033[1;34m2)\033[m Mostrar todos os contatos
\033[1;34m3)\033[m Buscar contato
\033[1;34m4)\033[m Editar contato
\033[1;34m5)\033[m Ordenar contatos por nome
\033[1;34m6)\033[m Apagar contato
\033[1;31m7) Sair\033[34m
\033[1;34m=====================>>\033[m''', end=' ')

def meeting():
    print('\033[1;34m=======================================================\033[m')
    print('Seja bem-vindo a sua \033[1;34mAGENDA!\033[m')
    print('Desenvolvido por João Pedro Monção\033[34m(github.com/jpmoncao)\033[m')

if __name__ == '__main__':
    show_menu()