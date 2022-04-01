M = int(input())
N = int(input())
sosu = []
for i in range(M, N+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1

        if error == 0:
            sosu.append(i)
if not sosu:
    print(-1)
else:
    print(sum(sosu))
    print(min(sosu))
