class Fila:
    arr = []
    tamanho = 0
    inicio = 0
    fim = 0
    qtElementos = 0
    tipo = ""

    def __init__(self, tamanhoFila) -> None:
        self.tamanho = tamanhoFila
        for i in range(self.tamanho):
            self.arr.append("")
        
    def Fila_Vazia(self):
        return True if self.qtElementos == 0 else False

    def Fila_Cheia(self):
        return True if self.qtElementos == self.tamanho else False

    def Enfileirar(self,elemento):
        self.tipo = type(elemento) if self.Fila_Vazia else self.tipo
        
        if not self.Fila_Cheia() and self.tipo == type(elemento):
            self.arr[self.inicio] = elemento
            self.inicio = 0 if self.inicio == self.tamanho - 1 else self.inicio + 1
            self.qtElementos += 1
        else:
            raise Exception("Fila está cheia")
            
    def desinfileirar(self):
        if not self.Fila_Vazia():
            self.fim = 0 if self.fim == self.tamanho-1 else self.fim + 1
            self.qtElementos -= 1
        else:
            raise Exception("A fila está vazia")
    
    def status(self):
        print(f'inicio {self.inicio} fim {self.fim} quantidade {self.qtElementos} fila {self.arr}')


n = Fila(3)
n.status()
n.Enfileirar(1)
n.status()
n.Enfileirar(2)
n.status()
n.Enfileirar(3)
n.status()
n.desinfileirar()
n.status()
n.Enfileirar(5)
n.status()
n.desinfileirar()
n.status()
n.desinfileirar()
n.status()
n.desinfileirar()
n.status()
n.desinfileirar()
n.status()