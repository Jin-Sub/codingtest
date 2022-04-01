N = int(input())
numbers = list(map(int, input().split()))
sosu = 0
for num in numbers:
    errors = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                errors += 1

        if errors == 0:
            sosu += 1

print(sosu)
