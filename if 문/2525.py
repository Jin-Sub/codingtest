a, b = list(map(int, input().split()))
c = int(input())
d = b + c
while(d >= 60):
    if a < 23:
        d = d-60
        a = a+1
    else:
        d = d - 60
        a = 0

print(a, d)
