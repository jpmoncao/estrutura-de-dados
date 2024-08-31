'''
Tarefa 5: Calculando o peso ideal
Crie um algoritmo que calcule o peso ideal de uma pessoa com base em sua altura e sexo. Use as fórmulas fornecidas para calcular o peso ideal para homens e mulheres.

Para concluir esta tarefa:

Leia a altura e o sexo da pessoa.
Use a fórmula apropriada com base no sexo da pessoa para calcular seu peso ideal.
- para homens: (72.7*h)-58

- para mulheres: (62.1*h)-44.7
'''

altura = float(input('Digite a altura: '))
sexo = int(input(
'''Digite o sexo:
    1) Homem
    2) Mulher
>> 
'''
))

if (sexo == 1):
    print(f'Para homens: {72.7 * altura - 58:.3f}')
elif (sexo == 2):
    print(f'Para mulheres: {62.1 * altura - 44.7:.3f}')
else:
    print('Código para sexo inválido!')
