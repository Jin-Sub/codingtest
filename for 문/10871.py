A, X = map(int, input().split())
N = list(map(int, input().split()))

for i in range(A):
    if N[i] < X:
        print(N[i], end=" ")
