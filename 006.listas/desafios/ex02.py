'''
2. Listas e Funções
Crie uma função chamada estatisticas que recebe uma lista de números inteiros e retorna a soma, o menor número, o maior número e a média da lista. O programa deve solicitar ao usuário que insira 10 números para a lista e, em seguida, exiba os resultados obtidos pela função.
'''

def estatisticas(numeros):
    return {
        'soma': sum(numeros),
        'menor': min(numeros),
        'maior': max(numeros),
        'media': sum(numeros) / len(numeros),
    }



numeros = []
for c in range(0,10):
    numero = int(input(f'Digite o {c+1}º número: '))
    numeros.append(numero)

resultado_estatisticas = estatisticas(numeros)

print(f' Soma: {resultado_estatisticas['soma']}')
print(f'Menor: {resultado_estatisticas['menor']}')
print(f'Maior: {resultado_estatisticas['maior']}')
print(f'Média: {resultado_estatisticas['media']}')
