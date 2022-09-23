def bubbleSort(A):
    for i in range(1,len(A)):
        for j in range(len(A)-1,0,-1*(i+1)):
            print(j)
            if A[j] < A[j-1]:
                aux = A[j]
                A[j] = A[j-1]
                A[j-1] = aux
    return a
a = [3,5,4,1,8,5]

print(bubbleSort(a))