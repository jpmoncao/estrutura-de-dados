'''
Tarefa 3: Classificando a idade do nadador
Você é obrigado a desenvolver um algoritmo que classifique um nadador em categorias de idade específicas com base em sua idade. As categorias e suas faixas etárias correspondentes são fornecidas.

Para concluir esta tarefa:

Leia a idade do nadador.
Determine em qual categoria o nadador se enquadra com base nas faixas etárias fornecidas.
Classifique o nadador na categoria apropriada:
infantil A =  5 -  7 anos
infantil B =  8 - 10 anos
juvenil A = 11 - 13 anos
juvenil B = 14 - 17 anos
adulto = maiores de 18 anos

'''

idade = int(input('Digite a idade do nadador: '))

if (idade > 4 and idade < 8):
    print('Infantil A')
elif (idade > 7 and idade < 11):
    print('Infantil B')
elif (idade > 10 and idade < 14):
    print('Juvenil A')
elif (idade > 13 and idade < 18):
    print('Juvenil B')
elif (idade >= 18):
    print('Adulto')
else:
    print('Não há categoria adequada para o nadador...')
