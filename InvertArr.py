arr = [1,2,3,4,5]	
def arrInvert(arr):
    inicio = 0
    fim = len(arr)-1
    while inicio < fim:
        arr[inicio], arr [fim] = arr[fim], arr[inicio]
        inicio += 1
        fim -= 1
    return arr
print (arrInvert(arr))