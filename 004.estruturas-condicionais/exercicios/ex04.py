'''
Tarefa 4: Calculando a quantidade da lanchonete
Desenvolva um algoritmo que leia o código de um item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. Use o menu fornecido para calcular o valor do item pedido.

Para concluir esta tarefa:

Leia o código do item e a quantidade encomendada.
Use o menu fornecido para encontrar o preço do item pedido.
Calcule o valor total a ser pago pelo lanche.
'''

print('''
============ CARDÁPIO =============
Especificação     Código      Preço
Cachorro quente      100       1,20
Bauru simples        101       1,30
Bauru com ovo        102       1,50
Hambúrger            103       1,20
Cheeseburguer        104       1,30
Refrigerante         105       1,00
''')

item_codigo = int(input('Digite o item: '))

comidas = [
    {'nome': 'Cachorro quente', 'codigo': 100, 'preco': 1.20},
    {'nome': 'Bauru simples'  , 'codigo': 101, 'preco': 1.30},
    {'nome': 'Bauru com ovo'  , 'codigo': 102, 'preco': 1.50},
    {'nome': 'Hambúrger'      , 'codigo': 103, 'preco': 1.20},
    {'nome': 'Cheeseburguer'  , 'codigo': 104, 'preco': 1.30},
    {'nome': 'Refrigerante'   , 'codigo': 105, 'preco': 1.00}
]

item_existe = False
for comida in comidas: 
    if comida.get('codigo') == item_codigo:
        item_existe = True
        quantidade = float(input('Digite a quantidade do item: '))
        preco_total = comida.get('preco') * quantidade

        print(f'O item {comida.get('nome')} custa R${preco_total:.2f}')

if (not item_existe):
    print('Item não existe!')
