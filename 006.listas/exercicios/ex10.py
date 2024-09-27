'''
10. Média e Manipulação de Listas
Peça ao usuário para inserir 5 notas (entre 0 e 10) e armazene-as em uma lista chamada notas. Calcule a média das notas e exiba as notas que são maiores do que a média.
'''

notas = []

while len(notas) < 5:
    nota = int(input(f'Digite uma nota: '))
    if 0 <= nota <= 10:
        notas.append(nota)

media = sum(notas) / len(notas)
notas_acima_media = [nota for nota in notas if nota > media]

print(f'A média é: {media}')
print(f'As notas acima da média são: {notas_acima_media}')
