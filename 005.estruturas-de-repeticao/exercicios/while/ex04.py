'''
4. (WHILE) Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um algoritmo que informe de 15 pessoas:  

a) a média de salário do grupo;

b) maior e menor idade do grupo;

c) quantidade de mulheres com salário até R$100,00.
'''
maior_idade = 0
menor_idade = 0
soma_salario = 0
escravas = 0
num_pessoas = 1

while num_pessoas <= 15:
    print(f'PESSOA {num_pessoas}/15')

    idade = int(input('Digite sua idade: '))

    if num_pessoas == 1:
        maior_idade = idade
        menor_idade = idade
    else:
        if maior_idade < idade:
            maior_idade = idade
        if menor_idade > idade:
            menor_idade = idade

    sexo = -1
    while sexo not in [1,2]:
        print('>> SEXO <<    \n'+
            ' 1) Masculino \n'+
            ' 2) Feminino    ')
        sexo = int(input('>> '))

    salario = float(input('Digite seu salário: '))

    if salario <= 100 and sexo == 2:
        escravas += 1

    soma_salario += salario
    num_pessoas += 1

print(
f'''    a) a média de salário do grupo: R${soma_salario / num_pessoas:.2f}
    b) maior idade do grupo: {maior_idade}
    b) menor idade do grupo: {menor_idade}
    c) quantidade de mulheres com salário até R$100,00: {escravas}'''
)