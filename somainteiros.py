## retirado do livro https://www.ime.usp.br/~pf/livrinho-AA/downloads/AA-BOOKLET.pdf#page=11

def SOMAPOSITIVOS (A, n):
    if n == 0:
        return 0
    else:
        n = n-1
        s  = SOMAPOSITIVOS (A, n)
    if A[n] > 0:
        return s + A[n]
    else:
        return s


print(SOMAPOSITIVOS([1,2,3,4,5,6,7,8,9], 9))