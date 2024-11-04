class Aluno:
    def __init__(self, nome, matricula, media):
        self.nome = nome
        self.matricula = matricula
        self.media = media

    def exibir_status(self):
        if (self.media >= 6):
            print(f'{self.nome:20} | RM: {self.matricula:6} | \033[32mAprovado\033[m')
        else:
            print(f'{self.nome:20} | RM: {self.matricula:6} | \033[31mReprovado\033[m')

aluno_aprovado = Aluno('João, o dedicado', '00569', 10)
aluno_reprovado = Aluno('José, o patife', '83103', 3)

aluno_aprovado.exibir_status()
aluno_reprovado.exibir_status()
