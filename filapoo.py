class Fila:
    
    def __init__(self, tamanhofila) -> None:
        self.__tamanho = tamanhofila
        self.__arr = []
        self.__inicio = 0
        self.__fim = 0
        self.__qtelementos = 0
        self.tipo = ""

        for i in range(self.__tamanho):
            self.__arr.append("")
        
    def filavazia(self):
        return True if self.__qtelementos == 0 else False

    def filacheia(self):
        return True if self.__qtelementos == self.__tamanho else False

<<<<<<< HEAD
    def Enfileirar(self,elemento):
        self.tipo = type(elemento) if self.Fila_Vazia else self.tipo
        
        if not self.Fila_Cheia() and self.tipo == type(elemento):
            self.arr[self.inicio] = elemento
            self.inicio = 0 if self.inicio == self.tamanho - 1 else self.inicio + 1
            self.qtElementos += 1
=======
    def enfileirar(self,elemento):
        if not self.filacheia():
            self.__arr[self.__inicio] = elemento
            self.__inicio = 0 if self.__inicio == self.__tamanho - 1 else 1 + self.__inicio
            self.__qtelementos += 1
>>>>>>> 50ac70dff8634c30b768690fcb1b15abd0fe721d
        else:
            raise Exception("Fila está cheia")
        

    def desinfileirar(self):
        if not self.filavazia():
            item = self.__arr[self.__fim]
            self.__fim = 0 if self.__fim == self.__tamanho-1 else self.__fim + 1
            self.__qtelementos -= 1
            return item
        else:
            raise Exception("A fila está vazia")
    
    def status(self):
        print(f'inicio {self.__inicio} fim {self.__fim} quantidade {self.__qtelementos} fila {self.__arr}')


n = Fila(3)
n.status()
n.enfileirar(1)
n.enfileirar(2)
n.enfileirar(3)
n.status()

print(n.desinfileirar())