class array:

    def __init__(self, array):
        self.arr = [*array]
        self.sort()
    def insert(self, value):
        self.arr = [*self.arr, value]
        self.sort()
    def removeByIndice(self, indice):
        if indice <= len(self.arr):
            self.arr = [*self.arr[0:indice], *self.arr[indice+1:len(self.arr)]]
        else:
            print("Erro: indice não encontrado")

    def removeByValue(self, value):
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                self.removeByIndice(i)
                break
    def sort(self):
        self.quickSortHelper(0, len(self.arr)-1)
    
    def quickSortHelper(self, first, last):
        if first < last:
            splitpoint = self.partition(first, last)
            self.quickSortHelper(first, splitpoint-1)
            self.quickSortHelper(splitpoint+1, last)
    def partition(self, first, last):
        pivotvalue = self.arr[first]
        leftmark = first+1
        rightmark = last
        done = False
        while not done:
            while leftmark <= rightmark and self.arr[leftmark] <= pivotvalue:
                leftmark = leftmark + 1
            while self.arr[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1
            if rightmark < leftmark:
                done = True
            else:
                temp = self.arr[leftmark]
                self.arr[leftmark] = self.arr[rightmark]
                self.arr[rightmark] = temp
        temp = self.arr[first]
        self.arr[first] = self.arr[rightmark]
        self.arr[rightmark] = temp
        return rightmark

arr = array([])

arr.insert(240)
print(arr.arr)
arr.removeByValue(5)
print(arr.arr)
arr.removeByValue(101)
print(arr.arr)
arr.removeByValue(240)
print(arr.arr)
