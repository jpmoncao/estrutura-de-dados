'''
8. (WHILE)Escrever um algoritmo que calcule e mostre a média aritmética dos números lidos entre 13 e 73.
'''

numero = 13
soma_numeros = 0
qtde_numeros = 0

while True:
    if numero > 73:
        break
    
    soma_numeros += numero
    qtde_numeros += 1
    numero += 1

print('Média aritmética dos números lidos entre 13 e 73: ' + str(soma_numeros / qtde_numeros))
