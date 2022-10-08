tamanho = 0
inicio = 0
fim = -1
num_elementos = 0

def Fila_Criar(tamanhoFila, tipoFila):
    global tamanho, valor_Inicial
    match tipoFila:
        case "I": valor_Inicial = 0
        case "F": valor_Inicial = float(0)
        case "S": valor_Inicial = ""
        case _: return "Tipo inválido"
    fila = []
    tamanho = tamanhoFila
    for i in range(tamanho):
        fila.append(valor_Inicial)
    return fila

def Fila_Cheia():
   return tamanho == num_elementos
   
def Fila_Vazia():
    global num_elementos
    return num_elementos == 0

def Enfileirar(fila, elemento):
    global fim, num_elementos
    if Fila_Cheia() == False and type(elemento) == type(fila[0]):
        if fim == tamanho -1:
            fim = 0
        else:
            fim += 1
        fila[fim] = elemento
        num_elementos += 1 
        return fila
    else:
        return "Tipo de dado inválido ou pilha cheia"
        
def desinfileirar():
    global inicio, tamanho, num_elementos
    if Fila_Vazia() == False:
        if inicio == tamanho -1:
            inicio = 0
        else:
            inicio += 1
        num_elementos -= 1

def mostrainicio(fila):
    return fila[inicio]

novaFila = Fila_Criar(3,"I")

Enfileirar(novaFila,1)
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
desinfileirar()
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
print(novaFila)

Enfileirar(novaFila,2)
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
desinfileirar()
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
print(novaFila)

Enfileirar(novaFila,3)
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
desinfileirar()
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
print(novaFila)

Enfileirar(novaFila,4)
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
desinfileirar()
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
print(novaFila)
Enfileirar(novaFila,5)
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
desinfileirar()
print(f"inicio {inicio} fim {fim} tamanho {tamanho}")
print(novaFila)

