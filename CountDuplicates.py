arr = []
def counter(arr):
    rept = 0
    for i in (range(len(arr))):
        for y in range(i+1,len(arr)):
            if (arr[i] == arr[y]) :
                rept += 1      
    return rept
print (counter(arr))