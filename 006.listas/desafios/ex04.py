'''4. Jogo da Forca com Listas
Crie um jogo da forca utilizando listas. O programa deve selecionar uma palavra aleatória de uma lista pré-definida de palavras. O jogador terá 6 tentativas para adivinhar a palavra. O jogo deve exibir as letras já acertadas e as tentativas restantes. Utilize uma lista para armazenar as letras já acertadas e outra para as letras erradas.
'''
from random import sample

palavras = ['python','java','javascript','ruby','golang','pascal','cobol','fortran','swift','kotlin','haskell','typescript','dart','rust','perl','elixir','scala','objectivec','assembly','lua','matlab','groovy','delphi','fsharp','csharp','erlang','julia','ocaml','crystal','lisp','elm','postscript','mercury','clojure']

PALAVRA_ESCOLHIDA = (sample(palavras, 1))[0]

def desenhar_forca(letra=''):
    letras_acertadas_ocultas = [letra if letra in letras_acertadas else '_' for letra in PALAVRA_ESCOLHIDA]
    palavra_oculta = '\033[1;33m' + ' '.join(letras_acertadas_ocultas) + '\033[m'
    palavra_forca = ''

    print(  '\n--------------------------')
    if len(letras_erradas) > 0:
        palavra_forca = 'FORCA'[0:len(letras_erradas)]
        print(f'\033[1;31m          {', '.join(letras_erradas)}\033[m')
    print( ' _____                     ')  
    print( '|     |                    ')
    print(f'|   {palavra_forca:5}      ')
    print( '|                          ')
    print(f'| {palavra_oculta}         ')
    print(  '--------------------------')

def verificar_letra(letra):
    letra = letra.lower()

    if len(letra) != 1 or letra.isnumeric():
        print('\033[1;31mLetra não informada/inválida!\033[m')
        input('\033[1m[Pression "Enter" para continuar]\033[m')
        return False

    letras = letras_erradas + letras_acertadas
    if letra in letras:
        print('\033[1;31mLetra já escrita!\033[m')
        input('\033[1m[Pression "Enter" para continuar]\033[m')
        return False

    if letra in PALAVRA_ESCOLHIDA:
        letras_acertadas.append(letra)
    else:
        letras_erradas.append(letra)

    for letra in PALAVRA_ESCOLHIDA:
        if letra not in letras_acertadas:
            return False
    return True

letras_acertadas = []
letras_erradas = []

while True:
    desenhar_forca()
    letra = str(input('Letra: '))
    
    if verificar_letra(letra):
        print(f'\033[1;32mVocê acertou! A palavra era "{PALAVRA_ESCOLHIDA}"!\033[m')
        break

    if len(letras_erradas) >= 5:
        print(f'\033[1;31mHAHA, você perdeu! A palavra era "{PALAVRA_ESCOLHIDA}"\033[m')
        break
