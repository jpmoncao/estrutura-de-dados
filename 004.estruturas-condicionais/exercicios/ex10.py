'''
Tarefa 10: Convertendo Dias em Anos, Meses e Dias

Faça um algoritmo que leia a idade de uma pessoa expressa em dias e a mostre expressa em anos, meses e dias.

Para concluir esta tarefa:
Leia a idade da pessoa em dias.

Converta a idade em anos, meses e dias.

Exiba a idade expressa em anos, meses e dias.
'''

print('-=-=Calculdadora de idade em anos, meses e dias=-=-')
dias_idade = int(input('Digite a idade em dias: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

anos_idade = dias_idade // 365
meses_idade = (dias_idade % 365) // 30
dias_idade = (dias_idade % 365) % 30

print(f'{anos_idade}  {meses_idade}  {dias_idade}')
