class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.head
        self.head = novo_no
        print(f"{valor} inserido no início.")

    def inserir_fim(self, valor):
        novo_no = No(valor)
        if not self.head:
            self.head = novo_no
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        print(f"{valor} inserido no fim.")

    def remover_inicio(self):
        if not self.head:
            print("A lista está vazia.")
        else:
            removido = self.head.valor
            self.head = self.head.proximo
            print(f"{removido} removido do início.")

    def remover_fim(self):
        if not self.head:
            print("A lista está vazia.")
        else:
            atual = self.head
            if not atual.proximo:
                removido = atual.valor
                self.head = None
            else:
                while atual.proximo.proximo:
                    atual = atual.proximo
                removido = atual.proximo.valor
                atual.proximo = None
            print(f"{removido} removido do fim.")

    def mostrar(self):
        if not self.head:
            print("A lista está vazia.")
        else:
            atual = self.head
            print("Lista encadeada:", end=" ")
            while atual:
                print(atual.valor, end=" -> ")
                atual = atual.proximo
            print("None")

    def buscar(self, valor):
        atual = self.head
        while atual:
            if atual.valor == valor:
                print(f"{valor} encontrado na lista.")
                return
            atual = atual.proximo
        print(f"{valor} não encontrado na lista.")


def menu_encadeada():
    print("\n--- Menu Lista Encadeada ---")
    print("[1] Inserir no início")
    print("[2] Inserir no fim")
    print("[3] Remover do início")
    print("[4] Remover do fim")
    print("[5] Mostrar lista")
    print("[6] Buscar elemento")
    print("[7] Sair")
    return int(input("Escolha uma opção: "))

lista_encadeada = ListaEncadeada()
while True:
    opcao = menu_encadeada()
    if opcao == 1:
        item = input("Digite o item para inserir no início: ")
        lista_encadeada.inserir_inicio(item)
    elif opcao == 2:
        item = input("Digite o item para inserir no fim: ")
        lista_encadeada.inserir_fim(item)
    elif opcao == 3:
        lista_encadeada.remover_inicio()
    elif opcao == 4:
        lista_encadeada.remover_fim()
    elif opcao == 5:
        lista_encadeada.mostrar()
    elif opcao == 6:
        item = input("Digite o item para buscar: ")
        lista_encadeada.buscar(item)
    elif opcao == 7:
        print("Encerrando...")
        break
