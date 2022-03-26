num = int(input())
for a in range(0, num):
    A, B = list(map(str, input().split()))
    c = ''
    for i in range(0, len(B)):
        for j in range(0, int(A)):
            c += (B[i])
    print(c)
