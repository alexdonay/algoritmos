arr = []
rept = []
def counter(arr):
    for i in (range(len(arr))):
        for y in range(i+1,len(arr)):
            if (arr[i] == arr[y]) :
                rept.append(arr[y])       
    return rept

print (counter(arr))
