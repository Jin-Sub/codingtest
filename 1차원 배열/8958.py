N = int(input())
A = 0
sum = 0
for _ in range(0, N):
    Array = str(input())
    for i in range(0, len(Array)):
        if Array[i] == 'O':
            A += 1
            sum += A
        else:
            A = 0

    print(sum)
    sum = 0
    A = 0
