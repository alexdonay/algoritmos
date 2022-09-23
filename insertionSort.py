def insertion_sort(A):
    for j in range(2, len(a)):
        chave = A[j] 
        i = j - 1 
        while i >= 0 and A[i] > chave: 
            A[i + 1] = A[i] 
            i = i - 1 
        A[i + 1] = chave 
    return A
#teste
a  = [5,7,8,12,1,5]
print(insertion_sort(a))




