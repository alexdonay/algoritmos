def PISODELOG (n):
    if n == 1:
        return 0
    else:
        return PISODELOG (n/2) + 1

print(PISODELOG(3))