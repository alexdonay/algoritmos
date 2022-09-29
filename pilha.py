class pilhaCustomizada:
    pilha = []
    tamanho = -1
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def verificaVazio(self):
        return True if (len(self.pilha)==0) else False
    def verificaCheio(self):
        return True if (len(self.pilha)< self.tamanho) else False
    def adicionar(self, value):
        if(self.verificaCheio()):
            self.pilha.append(value)
        else:
            print("Pilha cheia")
    def remover(self):
        if(self.verificaVazio()):
            print("Pilha Vazia")
        else:
            self.pilha.pop()
    def toString(self):
        return self.pilha
pilha = pilhaCustomizada(3)

pilha.adicionar(1)
pilha.adicionar(3)
print(pilha.toString())

pilha.remover()
print(pilha.pilha)
pilha.remover()
print(pilha.pilha)
pilha.remover()
print(pilha.pilha)
pilha.adicionar(1)
pilha.adicionar(3)
print(pilha.pilha)
pilha.adicionar(1)
pilha.adicionar(3)
print(pilha.pilha)


