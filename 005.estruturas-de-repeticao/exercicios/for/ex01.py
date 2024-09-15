'''11.  (FOR) Pesquisa sobre Idade e Altura:
   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre a idade e altura. A prefeitura deseja saber:
   a) média da idade da população;
   b) média da altura da população;
   c) maior idade registrada;
   d) percentual de pessoas com altura acima de 1,80 metros.
   O final da leitura de dados se dará com a entrada de uma idade negativa.
'''

idade = 0
altura = 0

soma_idade = 0
soma_altura = 0

maior_idade = 0
idade_acima_de_180cm = 0

qtde_pessoas = 0

while True:
   idade = int(input('Digite a idade [-1 para parar]: '))
   if idade < 0:
      break
   soma_idade += idade

   if qtde_pessoas == 0:
      maior_idade = idade
   else:
      if idade > maior_idade:
         maior_idade = idade

   altura = float(input('Digite a altura (m): '))
   soma_altura += altura

   if (altura > 1.80):
      idade_acima_de_180cm += 1

   qtde_pessoas += 1

if qtde_pessoas > 0:
   print(
f'''====== RESULTADO ======
   a) média da idade da população: {soma_idade / qtde_pessoas:.1f}
   b) média da altura da população: {soma_altura / qtde_pessoas:.2f}
   c) maior idade registrada: {maior_idade}
   d) percentual de pessoas com altura acima de 1,80 metros: {idade_acima_de_180cm * 100 / qtde_pessoas:.2f}%
'''
   )