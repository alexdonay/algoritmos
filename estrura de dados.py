# 1 tuplas
#tuplas não podem ser alteradas após serem declaradas
print("Tuplas")
tupla = ('a',1,2,4)
print(f"Tupla Inicializada - {tupla}")
#tupla[0] = 12 gera erro TypeError: 'tuple' object does not support item assignment
print(f"retorna o indice do valor 'a'{tupla.index('a')}") # retorna o indice do valor "A"

#2 Listas
# Listas permitem, adicionar, alterar, excluir e consultar itens
print("Listas")
lista = [1,2,3,4,5]
print(f"Lista inicializada - {lista}")
lista.pop(0) #remove indice zero
print(f'removendo indice 0 {lista}')
lista.append(12)
print(f'Adicionando o ítem 12 {lista}')
print(f'Pesquisando o indice do item com valor 2  {lista.index(2)}')
lista[0] = 15
print(f'Alterado o item 15 {lista}')

#3 Dicionários
#Dicionários são estruturas com Chave e Valor que podem ser altaradas 
print("Dicionário")
dic = {"valor1":1, "valor2":2}
print(f'Imprimindo Dicioinario {dic}')
dic['valor1'] = 3
print(f'Imprimindo e alterado o valor1 do dicionario - {dic["valor1"]}')
dic['valor3'] = 5

print(f'Imprimindo Dicioinario adcionado a chave valor3 {dic}')
#depois do método Del o dicionario passa a ter um comportamento de não auto completa com as propriedades e funções do dicionário

del(dic['valor1'])
dic['valor2'] = 3
print(f'Imprimindo Dicioinario {dic} excluindo valor1')




