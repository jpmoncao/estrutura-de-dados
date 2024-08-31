'''
Tarefa 6: Calculando o Preço Total
Um vendedor precisa de um algoritmo para calcular o preço total devido por um cliente. O algoritmo deve receber o código de um produto e a quantidade comprada e calcular o preço total usando a tabela fornecida de códigos de produto e preços unitários.

Para concluir esta tarefa:

Leia o código do produto e a quantidade comprada.
Use a tabela fornecida para encontrar o preço unitário do produto.
Calcule o preço total com base no preço unitário e na quantidade comprada.
Código do Produto Preço unitário
1001              5,32
1324              6,45
6548              2,37
0987              5,32
7623              6,45
'''

print('''
=============PRODUTOS============
Cód. do Produto   Preço unitário
1001              5,32
1324              6,45
6548              2,37
0987              5,32
7623              6,45
''')

produtos = [
    {'codigo': '1001', 'preco': 5.32},
    {'codigo': '1324', 'preco': 6.45},
    {'codigo': '6548', 'preco': 2.37},
    {'codigo': '0987', 'preco': 5.32},
    {'codigo': '7623', 'preco': 6.45}
]

produto_existe = False
codigo_produto = str(input('Digite um código: '))

for produto in produtos: 
    if produto.get('codigo') == codigo_produto:
        produto_existe = True
        quantidade = float(input('Digite a quantidade do item: '))
        preco_total = produto.get('preco') * quantidade

        print(f'O produto custará R${preco_total:.2f}')

if (not produto_existe):
    print('Produto não existe!')
