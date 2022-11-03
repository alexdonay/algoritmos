# Criado por: profa. Divani Barbosa Gavinier
# Adaptado por Alexsander Batista Donay

class No:
    def __init__(self, key = None, direita = None, esquerda =None):
        self.item = key
        self.direita = direita
        self.esquerda = esquerda


class Tree:

    def __init__(self):
        self.raiz = No()
        self.raiz = None

    def inserir(self, v):
        novo = No(v)  # cria um novo Nó
        if self.raiz == None:
            self.raiz = novo
        else:  # se nao for a raiz
            atual = self.raiz
            while True:
                anterior = atual
                if v <= atual.item:  # ir para esquerdauerda
                    atual = atual.esquerda
                    if atual == None:
                        anterior.esquerda = novo
                        return
                # fim da condição ir a esquerdauerda
                else:  # ir para direitaeita
                    atual = atual.direita
                    if atual == None:
                        anterior.direita = novo
                        return
                # fim da condição ir a direitaeita

    def buscar(self, chave):
        if self.raiz == None:
            return None  # se arvore vazia
        atual = self.raiz  # começa a procurar desde raiz
        while atual.item != chave:  # enquanto nao encontrou
            if chave < atual.item:
                atual = atual.esquerda  # caminha para esquerdauerda
            else:
                atual = atual.direita  # caminha para direitaeita
            if atual == None:
                return None  # encontrou uma folha -> sai
        return atual  # terminou o laço while e chegou aqui é pq encontrou item

    # O sucessor é o Nó mais a esquerdauerda da subarvore a direitaeita do No que foi passado como parametro do metodo
    def nosucessor(self, apaga):  # O parametro é a referencia para o No que deseja-se apagar
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.direita  # vai para a subarvore a direitaeita

        while atual != None:  # enquanto nao chegar no Nó mais a esquerdauerda
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esquerda  # caminha para a esquerdauerda

        # *********************************************************************************
        # quando sair do while "sucessor" será o Nó mais a esquerdauerda da subarvore a direitaeita
        # "paidosucessor" será o o pai de sucessor e "apaga" o Nó que deverá ser eliminado
        # *********************************************************************************
        if sucessor != apaga.direita:  # se sucessor nao é o filho a direitaeita do Nó que deverá ser eliminado
            # pai herda os filhos do sucessor que sempre serão a direitaeita
            paidosucessor.esquerda = sucessor.direita
            # lembrando que o sucessor nunca poderá ter filhos a esquerdauerda, pois, ele sempre será o
            # Nó mais a esquerdauerda da subarvore a direitaeita do Nó apaga.
            # lembrando também que sucessor sempre será o filho a esquerdauerda do pai
            sucessor.direita = apaga.direita  # guardando a referencia a direitaeita do sucessor para
            # quando ele assumir a posição correta na arvore
        return sucessor

    def remover(self, v):
        if self.raiz == None:
            return False  # se arvore vazia
        atual = self.raiz
        pai = self.raiz
        filho_esquerda = True
        # ****** Buscando o valor **********
        while atual.item != v:  # enquanto nao encontrou
            pai = atual
            if v < atual.item:  # caminha para esquerdauerda
                atual = atual.esquerda
                filho_esquerda = True  # é filho a esquerdauerda? sim
            else:  # caminha para direitaeita
                atual = atual.direita
                filho_esquerda = False  # é filho a esquerdauerda? NAO
            if atual == None:
                return False  # encontrou uma folha -> sai
        # fim laço while de busca do valor

        # **************************************************************
        # se chegou aqui quer dizer que encontrou o valor (v)
        # "atual": contem a referencia ao No a ser eliminado
        # "pai": contem a referencia para o pai do No a ser eliminado
        # "filho_esquerda": é verdadeiro se atual é filho a esquerdauerda do pai
        # **************************************************************

        # Se nao possui nenhum filho (é uma folha), elimine-o
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None  # se raiz
            else:
                if filho_esquerda:
                    pai.esquerda = None  # se for filho a esquerdauerda do pai
                else:
                    pai.direita = None  # se for filho a direitaeita do pai

        # Se é pai e nao possui um filho a direitaeita, substitui pela subarvore a direitaeita
        elif atual.direita == None:
            if atual == self.raiz:
                self.raiz = atual.esquerda  # se raiz
            else:
                if filho_esquerda:
                    pai.esquerda = atual.esquerda  # se for filho a esquerdauerda do pai
                else:
                    pai.direita = atual.esquerda  # se for filho a direitaeita do pai

        # Se é pai e nao possui um filho a esquerdauerda, substitui pela subarvore a esquerdauerda
        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita  # se raiz
            else:
                if filho_esquerda:
                    pai.esquerda = atual.direita  # se for filho a esquerdauerda do pai
                else:
                    pai.direita = atual.direita  # se for  filho a direitaeita do pai

        # Se possui mais de um filho, se for um avô ou outro grau maior de parentesco
        else:
            sucessor = self.nosucessor(atual)
            # Usando sucessor que seria o Nó mais a esquerdauerda da subarvore a direitaeita do No que deseja-se remover
            if atual == self.raiz:
                self.raiz = sucessor  # se raiz
            else:
                if filho_esquerda:
                    pai.esquerda = sucessor  # se for filho a esquerdauerda do pai
                else:
                    pai.direita = sucessor  # se for filho a direitaeita do pai
            # acertando o ponteiro a esquerdauerda do sucessor agora que ele assumiu
            sucessor.esquerda = atual.esquerda
            # a posição correta na arvore

        return True

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esquerda)
            print(atual.item, end=" ")
            self.inOrder(atual.direita)

    def preOrder(self, atual):
        if atual != None:
            print(atual.item, end=" ")
            self.preOrder(atual.esquerda)
            self.preOrder(atual.direita)

    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esquerda)
            self.posOrder(atual.direita)
            print(atual.item, end=" ")

    def altura(self, atual):
        if atual == None or atual.esquerda == None and atual.direita == None:
            return 0
        else:
            if self.altura(atual.esquerda) > self.altura(atual.direita):
                return 1 + self.altura(atual.esquerda)
            else:
                return 1 + self.altura(atual.direita)

    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esquerda == None and atual.direita == None:
            return 1
        return self.folhas(atual.esquerda) + self.folhas(atual.direita)

    def contarNos(self, atual):
        if atual == None:
            return 0
        else:
            return 1 + self.contarNos(atual.esquerda) + self.contarNos(atual.direita)

    def minn(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.esquerda
        return anterior

    def maxx(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.direita
        return anterior

    def caminhar(self):
        print(" Exibindo em ordem: ", end="")
        self.inOrder(self.raiz)
        print("\n Exibindo em pos-ordem: ", end="")
        self.posOrder(self.raiz)
        print("\n Exibindo em pre-ordem: ", end="")
        self.preOrder(self.raiz)
        print("\n Altura da arvore: %d" % (self.altura(self.raiz)))
        print(" Quantidade de folhas: %d" % (self.folhas(self.raiz)))
        print(" Quantidade de Nós: %d" % (self.contarNos(self.raiz)))
        if self.raiz != None:  # se arvore nao esta vazia
            print(" Valor minimo: %d" % (self.minn().item))
            print(" Valor maximo: %d" % (self.maxx().item))

#### fim da classe ####


arv = Tree()
print("Programa Arvore Binaria")
opcao = 0
while opcao != 5:
    print("***********************************")
    print("Entre com a opcao:")
    print(" --- 1: Inserir")
    print(" --- 2: Excluir")
    print(" --- 3: Pesquerdauisar")
    print(" --- 4: Exibir")
    print(" --- 5: Sair do programa")
    print("***********************************")
    opcao = int(input("-> "))
    if opcao == 1:
        x = int(input(" Informe o valor -> "))
        arv.inserir(x)
    elif opcao == 2:
        x = int(input(" Informe o valor -> "))
        if arv.remover(x) == False:
            print(" Valor nao encontrado!")
    elif opcao == 3:
        x = int(input(" Informe o valor -> "))
        if arv.buscar(x) != None:
            print(" Valor Encontrado")
        else:
            print(" Valor nao encontrado!")
    elif opcao == 4:
        arv.caminhar()
    elif opcao == 5:
        break
