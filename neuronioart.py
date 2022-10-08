from importlib.metadata import SelectableGroups


class neuronio:
    peso1 = 0.5
    peso2 = 0.5
    erro = 0
    taxaAprend = 0.1
    operadorE = [[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
    conjuntoTeste = [[0,0],[0,1],[1,0],[1,1]]
    
    def soma(self,entrada1, entrada2):
       soma = (entrada1*self.peso1) + (entrada2*self.peso2)
       return 1 if soma >=1 else 0

    def terminal(self):
        for i in range(0,4):
            if self.soma(self.conjuntoTeste[i][0],self.conjuntoTeste[i][1])!=self.operadorE[i][2]:
                return False
        return True

    def calcerro(self):
        self.erro = 0
        for i in range(0,4):
            self.erro -= abs(self.soma(self.conjuntoTeste[i][0],self.conjuntoTeste[i][1])-self.operadorE[i][2])
    
    def ajustaPesos(self):
        self.peso1 -= self.erro
        self.peso2 -= self.erro

neu = neuronio()

neu.calcerro()
neu.ajustaPesos()
print(neu.terminal())
print(f'erro{neu.erro} peso1 {neu.peso1} peso2 {neu.peso2}')

