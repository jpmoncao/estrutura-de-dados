def main():
    return 0

def load():
    bold('[Pressione "Enter" para continuar]', True)
    input(' ')
    print('')

def bold(msg, end=False):
    if end:
        print(f'\033[1m{msg}\033[m', end='')
    else:
        print(f'\033[1m{msg}\033[m')

def error(msg, end=False):
    if end:
        print(f'\033[1;31m{msg}\033[m', end='')
    else:
        print(f'\033[1;31m{msg}\033[m')

def warn(msg, end=False):
    if end:
        print(f'\033[1;33m{msg}\033[m', end='')
    else:
        print(f'\033[1;33m{msg}\033[m')

def linha_tabela():
    bold('-'*48)

if __name__ == '__main__':
    main()