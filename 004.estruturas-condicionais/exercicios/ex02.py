'''
Tarefa 2: Verificando múltiplos
Para esta tarefa, você desenvolverá um algoritmo que lê 2 valores (a e b) e determina se eles são múltiplos um do outro. Escreva-os com a mensagem "Eles são múltiplos" se forem múltiplos, ou "Eles não são múltiplos" se não forem.

Para concluir esta tarefa:

Leia os valores de a e b.
Verifique se um valor é um múltiplo do outro.
Anote os valores com a mensagem apropriada com base no resultado.

'''

a = int(input('Digite o nº a:'))
b = int(input('Digite o nº b:'))
multiplos = a % b == 0

if (multiplos):
    print("Eles são múltiplos")
else:
    print("Eles não são múltiplos")
    