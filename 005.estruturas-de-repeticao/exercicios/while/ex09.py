'''
9. (WHILE)Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.
'''

numero = 100
while True:
    if numero > 200:
        break
    if numero % 2 != 0:
        print(numero)
    numero += 1