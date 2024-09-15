'''
12.  (FOR) Pesquisa sobre Cor da Pele e Grau de Escolaridade:
   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre a cor da pele e grau de escolaridade. A prefeitura deseja saber:
   a) distribuição da população por cor da pele;
   b) percentual de pessoas com ensino superior completo;
   c) percentual de pessoas com ensino médio incompleto.
   A pesquisa termina quando for inserido o valor -1 para cor da pele.
'''

branco = preto = amarelo = outra_cor = 0
qtde_ensino_medio_incompleto = qtde_ensino_superior_completo = qtde_pessoas = 0

while True:
   cor_de_pele = 0
   while cor_de_pele not in [-1, 1, 2, 3, 4]:
      print(
f'''====COR==DE==PELE====
   1) Branco
   2) Preto
   3) Amarelo
   4) Outra cor
(-1 para finalizar)''')
      cor_de_pele = int(input('>> '))

   if cor_de_pele == -1:
      break
   elif cor_de_pele == 1:
      branco += 1
   elif cor_de_pele == 2:
      preto += 1
   elif cor_de_pele == 3:
      amarelo += 1
   elif cor_de_pele == 4:
      outra_cor += 1 

   grau_escolaridade = 0
   while grau_escolaridade not in range(1, 7):
      print(
f'''====GRAU DE ESCOLARIDADE====
   1) Ensino Fundamental incompleto
   2) Ensino Fundamental completo
   3) Ensino Médio incompleto
   4) Ensino Médio completo
   5) Ensino Superior incompleto
   6) Ensino Superior completo
'''
      )
      grau_escolaridade = int(input('>> '))

   if grau_escolaridade == 3:
      qtde_ensino_medio_incompleto += 1
   elif grau_escolaridade == 6:
      qtde_ensino_superior_completo += 1

   qtde_pessoas += 1

if qtde_pessoas > 0:
   print(
f'''====== RESULTADO ======
a) distribuição da população por cor da pele:
   branco: {branco * 100 / qtde_pessoas:.2f}%
   preto: {preto * 100 / qtde_pessoas:.2f}%
   amarelo: {amarelo * 100 / qtde_pessoas:.2f}%
   outras: {outra_cor * 100 / qtde_pessoas:.2f}%
b) percentual de pessoas com ensino superior completo: {qtde_ensino_medio_incompleto * 100 / qtde_pessoas:.2f}%
c) percentual de pessoas com ensino médio incompleto: {qtde_ensino_superior_completo * 100 / qtde_pessoas:.2f}%''')
