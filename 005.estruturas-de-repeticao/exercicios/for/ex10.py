'''
20. (FOR) Escreva um programa em C para imprimir uma pirâmide de números:  1
                                                                          2 2
                                                                         3 3 3
                                                                        4 4 4 4
                                                                       5 5 5 5 5
                                                                      6 6 6 6 6 6
                                                                     7 7 7 7 7 7 7
                                                                    8 8 8 8 8 8 8 8
                                                                   9 9 9 9 9 9 9 9 9
'''

for linha in range(1,10):
    linha_inteira = []
    for colunas in range(1, linha + 1):
        linha_inteira.append(linha)
    print(' ' * (9-linha), end="")
    print(*linha_inteira, sep=" ")
    