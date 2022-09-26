def buscaBinária(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2 
        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        if lista[pos_meio] < chave:
            pos_ini = pos_meio + 1

    return -1

chave = 15
lista = [1, 5,0 ,0,15, 20, 24, 45, 67, 76, 78, 100]
pos = buscaBinária(lista, chave)

print(pos)