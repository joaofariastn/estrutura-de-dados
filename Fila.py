from collections import deque

class Fila:
    def __init__(self):
        self.itens = deque()

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.popleft()

    def esta_vazia(self):
        return len(self.itens) == 0
dados = [64, 25, 12, 22, 11, 9]

fila = Fila()

for item in dados:
    fila.enfileirar(item)

while not fila.esta_vazia():
    print(fila.desenfileirar(), end=' ')
