a = int(input())
n = 0
b = a
c = 0
while True:
    c = (b // 10 + b % 10) % 10 + 10*(b % 10)
    n += 1
    b = c
    if a == b:
        break
print(n)
