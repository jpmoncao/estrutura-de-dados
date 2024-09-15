'''
15. (FOR) Pesquisa sobre Nível de Satisfação e Tempo de Residência:
   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o nível de satisfação com a cidade e tempo de residência. A prefeitura deseja saber:
   a) média do nível de satisfação da população;
   b) tempo de residência médio na cidade;
   c) percentual de pessoas insatisfeitas;
   d) percentual de pessoas que residem na cidade há mais de 10 anos.
   A pesquisa termina quando for inserido o valor -1 para o nível de satisfação.
'''

total_satisfacao = total_tempo_residencia = qtde_pessoas = qtde_insatisfeitas = qtde_residencia_mais_10_anos = 0

while True:
    nivel_satisfacao = int(input("Informe o nível de satisfação com a cidade (de 1 a 5 ou -1 para finalizar): "))

    if nivel_satisfacao == -1:
        break

    tempo_residencia = int(input("Informe o tempo de residência na cidade (em anos): "))

    qtde_pessoas += 1
    total_satisfacao += nivel_satisfacao
    total_tempo_residencia += tempo_residencia

    if nivel_satisfacao in [1, 2]:
        qtde_insatisfeitas += 1

    if tempo_residencia > 10:
        qtde_residencia_mais_10_anos += 1

media_satisfacao = total_satisfacao / qtde_pessoas if qtde_pessoas > 0 else 0
media_tempo_residencia = total_tempo_residencia / qtde_pessoas if qtde_pessoas > 0 else 0
percentual_insatisfeitas = qtde_insatisfeitas * 100 / qtde_pessoas if qtde_pessoas > 0 else 0
percentual_residencia_mais_10_anos = qtde_residencia_mais_10_anos * 100 / qtde_pessoas if qtde_pessoas > 0 else 0

if qtde_pessoas > 0:
    print(f'''
====== RESULTADO ======
a) Média do nível de satisfação da população: {media_satisfacao:.2f}
b) Tempo de residência médio na cidade: {media_tempo_residencia:.2f} anos
c) Percentual de pessoas insatisfeitas: {percentual_insatisfeitas:.2f}%
d) Percentual de pessoas que residem na cidade há mais de 10 anos: {percentual_residencia_mais_10_anos:.2f}%
''')
else:
    print("Nenhuma pessoa participou da pesquisa.")
