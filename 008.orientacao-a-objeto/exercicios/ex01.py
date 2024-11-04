class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_informacoes(self): 
        print(f'Livro: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano}')

livro1 = Livro('Eles precisam saber', 'Luca Martini', 2022)
livro2 = Livro('Cultura do Jejum', 'Luciano Subirá', 2023)
livro3 = Livro('Vimos e ouvimos', 'Israel Subirá', 2024)

livro1.exibir_informacoes()
livro2.exibir_informacoes()
livro3.exibir_informacoes()
