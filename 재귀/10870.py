def pivo(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = pivo(n-1)+pivo(n-2)
    return result


n = int(input())
print(pivo(n))
