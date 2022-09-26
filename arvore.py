class Item:
    def __init__(self, noAnterior, noAtual, valor, arvore):
        self.noAnterior = noAnterior
        self.noAtual = noAtual
        self.valor = valor
        arvore.append(self)
    def toString(self):
        return str(self.valor)
    
arvore = []
item =  Item(0,0,1, arvore)

print(item.toString())
