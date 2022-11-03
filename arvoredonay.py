class arvore:
    def __init__(self, chave, direita=None, esquerda=None):
        self.chave = None
        self.direita = None
        self.esquerda = None

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


def insere(nodo, raiz=None):
    if raiz == None:
        raiz = arvore(nodo)
    elif raiz.chave < nodo.chave:
        if raiz.direita == None:
            raiz.direita = nodo
        else:
            insere(nodo, raiz.direita)
    else:
        if raiz.esquerda == None:
            raiz.esquerda = nodo
        else:
            insere(nodo, raiz.esquerda)
    

insere(12)