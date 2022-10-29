import time
class Node:
     
    def __init__(self, chave = None, direita = None, esquerda= None):
        self.valor = chave
        self.dir = direita
        self.esq = esquerda
class Tree:
    def __init__(self):
        self.raiz = None
    def insert(self, valor):
        novo = Node(valor) 
        if self.raiz == None:
            self.raiz = novo
        else: 
            atual = self.raiz
            while True:
                anterior = atual
                if valor <= atual.valor: 
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return             
                else: 
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

    def search(self, chave):
        if self.raiz == None:
            return None 
        atual = self.raiz 
        while atual.valor != chave: 
            if chave < atual.valor:
                atual = atual.esq 
            else:
                atual = atual.dir 
                if atual == None:
                    return None
        return atual   
    def noSucessor(self, apaga): 
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir

        while atual != None: 
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq 

        if sucessor != apaga.dir: 
            paidosucessor.esq = sucessor.dir 
            sucessor.dir = apaga.dir 

        return sucessor

    def searchAndRemove(self, valor):
        if self.raiz == None:
            return False 
        atual = self.raiz
        pai = self.raiz
        filhoEsq = True


        while atual.valor!= valor:
            pai = atual
            if valor < atual.valor: 
                atual = atual.esq
                filhoEsq = True 
            else: 
                atual = atual.dir 
                filhoEsq = False 
            if atual == None:
                return False
         
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None 
            else:
                if filhoEsq:
                    pai.esq =  None 
                else:
                    pai.dir = None 

        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.esq 
            else:
                if filhoEsq:
                    pai.esq = atual.esq 
                else:
                    pai.dir = atual.esq 
         
        elif atual.esq == None:
            if atual == self.raiz:
                self.raiz = atual.dir 
            else:
                if filhoEsq:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir 

        else:
            sucessor = self.noSucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filhoEsq:
                    pai.esq = sucessor 
                else:
                    pai.dir = sucessor 
            sucessor.esq = atual.esq   

        return True
  
arvore = Tree()

