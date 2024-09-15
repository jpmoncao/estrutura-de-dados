'''
14. (FOR) Pesquisa sobre Profissão e Renda:
   A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre a profissão e renda mensal. A prefeitura deseja saber:
   a) média da renda mensal da população;
   b) profissão com maior média de renda;
   c) percentual de pessoas desempregadas;
   d) percentual de pessoas com renda acima de R$ 5000,00.
   A pesquisa termina quando for inserido o valor "x" para a renda.
'''

# Inicializa variáveis
qtde_pessoas = qtde_desempregados = qtde_renda_acima_5000 = 0
total_renda = 0
profissoes_renda = {}

while True:
    profissao = input("Informe a profissão (ou 'x' para finalizar): ").lower()

    if profissao == 'x':
        break

    renda = float(input("Informe a renda mensal: "))

    qtde_pessoas += 1
    total_renda += renda

    if profissao == 'desempregado':
        qtde_desempregados += 1

    if renda > 5000:
        qtde_renda_acima_5000 += 1

    if profissao in profissoes_renda:
        profissoes_renda[profissao]['soma_renda'] += renda
        profissoes_renda[profissao]['contagem'] += 1
    else:
        profissoes_renda[profissao] = {'soma_renda': renda, 'contagem': 1}

media_renda_populacao = total_renda / qtde_pessoas if qtde_pessoas > 0 else 0

maior_media_renda = 0
profissao_maior_media = ''

for profissao, dados in profissoes_renda.items():
    media_renda = dados['soma_renda'] / dados['contagem']
    if media_renda > maior_media_renda:
        maior_media_renda = media_renda
        profissao_maior_media = profissao

if qtde_pessoas > 0:
    print(f'''
====== RESULTADO ======
a) Média da renda mensal da população: R$ {media_renda_populacao:.2f}
b) Profissão com maior média de renda: {profissao_maior_media} (R$ {maior_media_renda:.2f})
c) Percentual de pessoas desempregadas: {qtde_desempregados * 100 / qtde_pessoas:.2f}%
d) Percentual de pessoas com renda acima de R$ 5000,00: {qtde_renda_acima_5000 * 100 / qtde_pessoas:.2f}%
''')
else:
    print("Nenhuma pessoa participou da pesquisa.")
