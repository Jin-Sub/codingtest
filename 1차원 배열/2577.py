A = int(input())
B = int(input())
C = int(input())
D = str(A*B*C)
E = [0]*10

for i in range(0, len(D)):
    j = int(D[i])
    E[j] += 1

for i in range(0, 10):
    print(E[i])
