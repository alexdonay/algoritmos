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
