class PilhaCuston:
    pilha = []
    tamanho = -1
    tipo = ""
    def __init__(self, tamanho):
        self.tamanho = tamanho
    def verificaCheio(self):
        return self.tamanho == len(self.pilha)
    def verificaVazio(self):
        return self.pilha==[]
    def verificaTipo(self, value):
        return self.tipo != type(value)
    def add(self, value):
        if(self.verificaVazio()):
            self.tipo = type(value)
            self.pilha.append(value)
        elif(self.verificaCheio() or self.verificaTipo(value)):
            print("estouro")
        else:
            self.pilha.append(value)
    def rm(self):
        if(self.verificaVazio()):
            print("pilha vazia")
        else:
            self.pilha.pop()
            

pi = PilhaCuston(2)

pi.add(2)

pi.rm()


print(pi.pilha)

for i in range(0,4):
    print(i)