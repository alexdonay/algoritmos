def fibonacciTopDown(n, table = {}):
    x = 0
    if n == 1 or n == 0:
        x += 1
        return n
    try:
        x += 1
        return table[n]
    except:
        table[n] = fibonacciTopDown(n-1) + fibonacciTopDown(n-2)
    x += 1
    print(f'repete {x}')
    return table[n]

print(fibonacciTopDown(15))
