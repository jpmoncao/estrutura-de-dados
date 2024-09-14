'''
3. (WHILE) Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0,25]:
[26,50], [51,75] e [76,100]. A entrada de dados deve terminar quando for lido um número negativo.
'''

num = 0
intervalos = [0, 0, 0, 0]

while num >= 0:
    num = int(input('Digite um número [-1 para encerrar]: '))
    if 0 < num <= 25:
        intervalos[0] += 1
    elif 26 <= num <= 50:
        intervalos[1] += 1
    elif 51 <= num <= 75:
        intervalos[2] += 1
    elif 76 <= num <= 100:
        intervalos[3] += 1

print(
f'''
<<<RESULTADO FINAL>>>
Números entre   [0,25]: {intervalos[0]} 
Números entre  [26,50]: {intervalos[1]}
Números entre  [51,75]: {intervalos[2]}
Números entre [76,100]: {intervalos[3]}
'''
)
