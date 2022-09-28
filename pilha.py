class pilhaCustomizada:
    pilha = []
    tamanho = -1
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def verificaVazio():
        return True if (len(pilha)==0) else False
    def verificaCheio():
        return True if (len(pilha)== tamanho) else False
    def adicionar(self, value):
        if(self.verificaCheio):
            self.pilha.append(value)
        else:
            print("Pilha cheia")
    def remover():
        if(self.verificaVazio):
            print("Pilha Vazia")
        else:
            self.pilha.remove()

pilha = pilhaCustomizada(9)



pilha.adicionar(1)
pilha.remover()
