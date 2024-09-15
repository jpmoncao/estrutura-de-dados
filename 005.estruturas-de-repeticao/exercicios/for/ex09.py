'''
19. (FOR) Faça um programa em C para calcular a potência de um número.
'''

numero = int(input('Digite um número: '))
potencia = int(input('Elevado a: '))

res = 1
if potencia < 0:
    numeros = range(potencia, 0)
else: 
    numeros = range(0, potencia)

for n in numeros:
    if potencia < 0:
        res /= numero
    else:
        res *= numero

print(f'{numero}^{potencia} = {res}')
