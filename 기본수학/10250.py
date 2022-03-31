A = int(input())

for i in range(A):
    H, W, N = map(int, input().split())
    line = 1
    while N > H:
        N -= H
        line += 1

    print(100*N+line)
