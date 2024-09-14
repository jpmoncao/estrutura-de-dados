'''
5. (WHILE) Faça um algoritmo que determine e escreva:  

- a maior idade dos habitantes

- a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros.

O final do conjunto de habitantes é reconhecido pelo valor -1 entrada como idade.
'''

idade = 0
dados = {
    'maior_idade': 0,
    'qtde_loiras_olhos_verde': 0
}

print('=== PESQUISA EXTREMAMENTE ESPECÍFICA ===')
while True:
    idade = int(input('Digite a idade [-1 para parar]: '))
    if idade < 0:
        break

    if dados['maior_idade'] == 0:
       dados['maior_idade'] = idade
    elif dados['maior_idade'] < idade:
       dados['maior_idade'] = idade

    sexo = -1
    while sexo not in [1,2]:
        print('>> SEXO <<    \n'+
              ' 1) Masculino \n'+
              ' 2) Feminino    ')
        sexo = int(input('>> '))
    print('========================================')

    cor_de_cabelo = -1
    while cor_de_cabelo not in [1,2,3,4,5]:
        print('>> COR DE CABELO <<   \n'+
              ' 1) Cabelos louros    \n'+
              ' 2) Cabelos castanhos \n'+
              ' 3) Cabelos ruivos    \n'+
              ' 4) Cabelos pretos    \n'+
              ' 5) Outra coloração     ')
        cor_de_cabelo = int(input('>> '))
    print('========================================')
    
    cor_dos_olhos = -1
    while cor_dos_olhos not in [1,2,3,4]:
        print('>> COR DE OLHOS <<   \n'+
              ' 1) Olho azul        \n'+
              ' 2) Olho castanho    \n'+
              ' 3) Olho verde       \n'+
              ' 4) Outra coloração    ')
        cor_dos_olhos = int(input('>> '))
    print('========================================')

    if sexo == 2 and (cor_de_cabelo == 1 and cor_dos_olhos == 3 and (18 <= idade <= 35)):
        dados['qtde_loiras_olhos_verde'] += 1

print(f'''Essa estranha pesquisa aponta o resultado que:
    A maior idade entre os habitantes é de: {dados["maior_idade"]}
    A quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros é de: {dados["qtde_loiras_olhos_verde"]}
    ''')