def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    tamanhoX = len(str(x))
    tamanhoY = len(str(y))
    maiorNumero = max(tamanhoX,tamanhoY)
    maiorNumerod2 = round(maiorNumero/2)
    divint1 = x // (10 ** maiorNumerod2)
    
    resto1 = x % (10 ** maiorNumerod2)
    divint2 = y // (10 ** maiorNumerod2)
    resto2 = y % (10 ** maiorNumerod2)
    divInt = Karatsuba(divint1, divint2)
    resto = Karatsuba(resto1, resto2)
    ad_plus_bc = Karatsuba(divint1 + resto1, divint2 + resto2) - divInt - resto
    return (10 ** (2*maiorNumerod2))*divInt + (10 ** maiorNumerod2)*ad_plus_bc + resto

print(Karatsuba(1234,5678))
print()
print(Karatsuba(350,250))
