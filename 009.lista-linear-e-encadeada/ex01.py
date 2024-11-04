class ListaLinear:
    def __init__(self):
        self.lista = []

    def inserir_inicio(self, valor):
        self.lista.insert(0, valor)
        print(f"{valor} inserido no início.")

    def inserir_fim(self, valor):
        self.lista.append(valor)
        print(f"{valor} inserido no fim.")

    def remover_inicio(self):
        if not self.lista:
            print("A lista está vazia.")
        else:
            removido = self.lista.pop(0)
            print(f"{removido} removido do início.")

    def remover_fim(self):
        if not self.lista:
            print("A lista está vazia.")
        else:
            removido = self.lista.pop()
            print(f"{removido} removido do fim.")

    def mostrar(self):
        if not self.lista:
            print("A lista está vazia.")
        else:
            print("Lista:", " -> ".join(map(str, self.lista)), "-> None")

    def buscar(self, valor):
        if valor in self.lista:
            print(f"{valor} encontrado na lista.")
        else:
            print(f"{valor} não encontrado na lista.")

def menu_lista_linear():
    print("\n--- Menu Lista Linear ---")
    print("[1] Inserir no início")
    print("[2] Inserir no fim")
    print("[3] Remover do início")
    print("[4] Remover do fim")
    print("[5] Mostrar lista")
    print("[6] Buscar elemento")
    print("[7] Sair")
    return int(input("Escolha uma opção: "))

# Programa principal
lista_linear = ListaLinear()
while True:
    opcao = menu_lista_linear()
    if opcao == 1:
        item = input("Digite o item para inserir no início: ")
        lista_linear.inserir_inicio(item)
    elif opcao == 2:
        item = input("Digite o item para inserir no fim: ")
        lista_linear.inserir_fim(item)
    elif opcao == 3:
        lista_linear.remover_inicio()
    elif opcao == 4:
        lista_linear.remover_fim()
    elif opcao == 5:
        lista_linear.mostrar()
    elif opcao == 6:
        item = input("Digite o item para buscar: ")
        lista_linear.buscar(item)
    elif opcao == 7:
        print("Encerrando...")
        break
