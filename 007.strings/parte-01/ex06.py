'''Exercício 6: Formatação do CPF
Seu objetivo é criar uma função que pegue uma sequência de números e a formate como um CPF brasileiro (XXX.XXX.XXX-XX). Isso significa que você precisará inserir a pontuação apropriada para formatar a string de entrada como um CPF.

Para concluir este exercício com êxito:

Defina uma função que receba uma sequência de números como entrada.
Implemente um método para formatar a string como um CPF brasileiro.
Retorne o CPF formatado como a saída da função.'''

def formatar_cpf(sequencia):
    return f'{sequencia[0:3]}.{sequencia[3:6]}.{sequencia[6:9]}-{sequencia[9:11]}'
    
cpf = input('CPF: ')
print(formatar_cpf(cpf))
