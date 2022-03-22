N = int(input())

for _ in range(0, N):
    sum = 0
    A = 0
    Array = list(map(int, input().split()))
    for i in range(1, len(Array)):
        sum += Array[i]

    sum /= Array[0]

    for i in range(1, len(Array)):
        if Array[i] > sum:
            A += 1

    A = A/Array[0]*100

    print(f'{A:.3f}%')
