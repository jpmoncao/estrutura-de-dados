'''
6. (WHILE) Escreva um algoritmo que gere o números de 1000 a 1999 e escreva aqueles que dividido por 11 dão resto igual a 5.
'''

numero = 1000

while True:
    if numero > 1999:
        break

    if numero % 11 == 5:
        print(numero)
    numero += 1
