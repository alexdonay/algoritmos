quant = 0
def bubbleSort(A):
    global quant
    for i in range(1,len(A)):
        for j in range(len(A)-1,0,-1*(i+1)):
            
            if A[j] < A[j-1]:
                aux = A[j]
                A[j] = A[j-1]
                A[j-1] = aux
                quant +=1
    return a
a = oo = [3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1,3,5,4,2,1]
print(bubbleSort(a))

    
print(quant)


print(quant)
print(quant)