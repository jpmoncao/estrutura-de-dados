'''
Tarefa 9: Convertendo idade em dias

Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre que ela é expressa apenas em dias.

Para concluir esta tarefa:
Leia a idade da pessoa em anos, meses e dias.

Converta a idade em dias.

Exiba a idade expressa em dias.
'''

print('-=-=Calculdadora de dias de idade=-=-')
anos = int(input('Digite os anos: '))
meses = int(input('Digite os meses: '))
dias = int(input('Digite os dias: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

anos_dias = anos * 365
meses_dias = meses * 30
dias += anos_dias + meses_dias

print(f'Os dias de idade com as informações inseridas são: {dias} dias.')
