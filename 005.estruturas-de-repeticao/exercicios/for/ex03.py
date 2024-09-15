'''
13. (FOR) Pesquisa sobre Sexo e Estado Civil:
   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o sexo e estado civil. A prefeitura deseja saber:
   a) distribuição da população por sexo;
   b) percentual de pessoas solteiras;
   c) quantidade de pessoas casadas;
   d) percentual de pessoas divorciadas.
   A pesquisa termina quando for inserido o valor "X" para o sexo.
'''

masculino = feminino = 0
qtde_solteiros = qtde_casados = qtde_divorciados = qtde_pessoas = 0

while True:
    sexo = ''
    while sexo not in ['M', 'F', 'X']:
        print(
            '''====SEXO====
   M) Masculino
   F) Feminino
(X para finalizar)'''
        )
        sexo = input('>> ').upper()

    if sexo == 'X':
        break
    elif sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1

    estado_civil = 0
    while estado_civil not in range(1, 5):
        print(
            '''====ESTADO CIVIL====
   1) Solteiro(a)
   2) Casado(a)
   3) Divorciado(a)
   4) Viúvo(a)'''
        )
        estado_civil = int(input('>> '))

    if estado_civil == 1:
        qtde_solteiros += 1
    elif estado_civil == 2:
        qtde_casados += 1
    elif estado_civil == 3:
        qtde_divorciados += 1

    qtde_pessoas += 1

if qtde_pessoas > 0:
    print(
        f'''====== RESULTADO ======
a) distribuição da população por sexo:
   masculino: {masculino * 100 / qtde_pessoas:.2f}%
   feminino: {feminino * 100 / qtde_pessoas:.2f}%
b) percentual de pessoas solteiras: {qtde_solteiros * 100 / qtde_pessoas:.2f}%
c) quantidade de pessoas casadas: {qtde_casados}
d) percentual de pessoas divorciadas: {qtde_divorciados * 100 / qtde_pessoas:.2f}%'''
    )
    