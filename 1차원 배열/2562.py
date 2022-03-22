num = []
for _ in range(0, 9):
    i = int(input())
    num.append(i)

print(max(num))
print(num.index(max(num))+1)
