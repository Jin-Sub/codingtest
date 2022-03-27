A, B = list(map(str, input().split()))

C = ''.join(reversed(A))
D = ''.join(reversed(B))

print(max(C, D))
