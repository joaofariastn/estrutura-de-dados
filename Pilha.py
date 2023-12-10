class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()

    def esta_vazia(self):
        return len(self.itens) == 0

# Exemplo de uso da Pilha
pilha = Pilha()
dados = [64, 25, 12, 22, 11, 9]

for item in dados:
    pilha.empilhar(item)

while not pilha.esta_vazia():
    print(pilha.desempilhar(), end=' ')
