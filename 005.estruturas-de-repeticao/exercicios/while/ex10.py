'''
10. (WHILE)Escrever um algoritmo que lê 10 valores, um de cada vez, e conta quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.
'''

dentro_do_intervalo = 0
fora_do_intervalo = 0

numero = 0
cont = 1
while cont <= 10:
    numero = int(input(f'Digite um número ({cont}/10): '))

    if 10 <= numero <= 20:
        dentro_do_intervalo += 1
    else:
        fora_do_intervalo += 1
    cont += 1

print(
f'''
Dentro do intervalo [10,20]: {dentro_do_intervalo}
Fora do intervalo: {fora_do_intervalo} 
'''
)