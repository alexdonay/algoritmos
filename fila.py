<<<<<<< HEAD
tamanho = 0
inicio = 0
fim = -1
num_elementos = 0

def Fila_Criar(tamanhoFila, tipoFila):
    global tamanho, valor_Inicial
    valor_Inicial = 0
    if tipoFila == "I":
        valor_Inicial = 0
    elif tipoFila == "F":
        valor_Inicial == float(0)
    elif tipoFila == "S":
        valor_Inicial = ""
    else:
        return "Tipo inválido"
    tamanho = tamanhoFila
    fila = []
    for i in range(tamanho):
        fila.append(valor_Inicial)
    return fila

def Fila_Cheia():
    if tamanho == num_elementos:
        return True
    else:
        return False
def Fila_Vazia():
    global num_elementos
    if num_elementos == 0:
        return True
    else:
        return False
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

def imprimirFila(fila):
    novafila = []
    global inicio, tamanho
    counter = 0 
    ponteiro = inicio
    while counter < tamanho:
        novafila.append(fila[ponteiro])
        if ponteiro == tamanho-1:
            ponteiro = 0
        else:
            ponteiro += 1
        counter += 1
    return novafila
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
print(imprimirFila(novaFila))
=======
fila = []
tipo =  ""
tamanho = 0
quantidade = 0
inicio = 0
fim = 0
def CriarFila(tamanhoFila, tipoFila):
    global fila, tipo, tamanho, quantidade, inicio, fim
    if tipoFila == "i" or "f" or "s":
        for i in range(tamanhoFila):
            fila.append("")
        tipo = tipoFila
        tamanho = tamanhoFila
        quantidade = 0
        inicio = 0
        fim = 0
    else:
        print("tipo inválido")

def Adcionar(valorDados, tipoDados):
    global fila, tipo, tamanho, quantidade, inicio, fim
    if tipoDados == tipo and quantidade <= tamanho - 1 :
        fila[fim] = valorDados
        quantidade += 1
        if fim == tamanho - 1:
            fim = 0
        else:
            fim += 1

def remover():
    global quantidade, inicio
    if quantidade>0:
        print(fila[inicio])
        fila[inicio] = ""
        quantidade -= 1
        if inicio  == tamanho -1 :
            inicio = 0
        else:
            inicio += 1
        
    else:
        print("fila vazia")


CriarFila(7,'i')

Adcionar(9, 'i')
print(f"{inicio} {fim}")
Adcionar(10, 'i')
print(f"{inicio} {fim}")
Adcionar(10, 'i')
print(f"{inicio} {fim}")
Adcionar(10, 'i')
print(f"{inicio} {fim}")
Adcionar(10, 'i')
print(f"{inicio} {fim}")
Adcionar(10, 'i')
print(f"{inicio} {fim}")
Adcionar(10, 'i')
print(f"{inicio} {fim}")
remover()
print(f"{inicio} {fim}")
remover()
print(f"{inicio} {fim}")
remover()
print(f"{inicio} {fim}")
remover()
print(f"{inicio} {fim}")
Adcionar(9, 'i')
print(f"{inicio} {fim}")

print(fila)
remover()

print(f"{inicio} {fim}")
remover()
print(f"{inicio} {fim}")
remover()
print(f"{inicio} {fim}")
Adcionar(9, 'i')
print(f"{inicio} {fim}")

print(fila)
>>>>>>> b1f8349725c2b972fba4ca489b53fec878839bc6
