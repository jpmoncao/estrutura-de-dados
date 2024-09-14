'''
7. (WHILE) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:  

a) média do salário da população;

b) média do número de filhos;

c) maior salário;

d) percentual de pessoas com salário até R$100,00.

O final da leitura de dados se dará com a entrada de um salário negativo.  
'''

num_pessoas = 0
num_pessoas_salario_ate_cem = 0
soma_numero_filhos = 0
soma_salario = 0
maior_salario = 0

salario = 0

while salario >= 0:
    salario = float(input('Digite seu salário [-1 para parar]: R$'))
    if salario > maior_salario:
        maior_salario = salario

    if salario < 0:
        break
    elif salario <= 100:
        num_pessoas_salario_ate_cem += 1

    soma_salario += salario
    soma_numero_filhos += int(input('Digite a qtde. de filhos: '))

    num_pessoas += 1

if (num_pessoas > 0):
    print(f'''=== RESULTADO PESQUISA ===
    b) média do número de filhos: {soma_numero_filhos / num_pessoas:.2f}
    a) média do salário da população: R${soma_salario / num_pessoas:.2f}
    c) maior salário: R${maior_salario:.2f}
    d) percentual de pessoas com salário até R$100,00: {num_pessoas_salario_ate_cem * 100 / num_pessoas:.2f}%
    ''')