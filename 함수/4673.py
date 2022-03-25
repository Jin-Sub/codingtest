def solve(n):
    return n + n % 10 + (n % 100) // 10 + (n//100) % 10 + (n // 1000)


d = [0]*10000

for i in range(0, 10000):
    if solve(i) < 10000:
        d[solve(i)] += 1

for i in range(0, 10000):
    if d[i] == 0:
        print(i)
