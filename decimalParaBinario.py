arr =[]
contador = 0
def DecimalParaBinario(valor):
    
    if valor//2>0:
        DecimalParaBinario(valor//2)
        arr.append(valor%2)
    else:
        arr.append(valor%2)

    return arr
       
print(DecimalParaBinario(327))

def converteBase(n)   :
    B = []
    i = 1
    t = n
    while t > 0.0:
        B.append(t%2)
        i += 1
        t = t//2
    return B

print(converteBase(327))