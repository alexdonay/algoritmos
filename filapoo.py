class Fila:
    arr = []
    tamanho = 0
    inicio = 0
    fim = 0
    qtElementos = 0
    tipo = ""
    def __init__(self, tipoDado, tamanhoFila) -> None:
        match tipoDado:
            case "I": valor_Inicial = 0
            case "F": valor_Inicial = float(0)
            case "S": valor_Inicial = ""
            case _: return "Tipo inválido"
        self.tamanho = tamanhoFila
        for i in range(self.tamanho):
            self.arr.append(valor_Inicial)
    def Fila_Cheia(self):
        return self.tamanho == self.qtElementos
    def Fila_Vazia(self):
        print(f"quantidade  {self.qtElementos}")
        return self.qtElementos == 0
    def Enfileirar(self,elemento):
        
        if self.Fila_Cheia() == False and type(elemento) == type(self.arr[0]):
            self.arr[self.fim] = elemento
            if self.fim == self.tamanho -1:
                self.fim = 0
            else:
                self.fim += 1
            self.qtElementos += 1
        else: 
            return "Tipo de dado inválido ou pilha cheia"
    def desinfileirar(self):
        if self.Fila_Vazia() == True:
            if self.inicio == self.tamanho -1:
                self.inicio = 0
        else:
            
            self.inicio += 1
            self.qtElementos -= 1
novaFila = Fila("I",2)
novaFila.Enfileirar(1)
print(f"quantidade de elementos {novaFila.qtElementos} fila {novaFila.arr}")
novaFila.Enfileirar(2)
print(f"qt {novaFila.qtElementos} {novaFila.arr}")
novaFila.desinfileirar()
print(f"qt {novaFila.qtElementos} {novaFila.arr}")
novaFila.Enfileirar(3)
print(f"qt {novaFila.qtElementos} {novaFila.arr}")
