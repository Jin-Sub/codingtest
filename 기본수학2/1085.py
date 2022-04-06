x, y, w, h = list(map(int, input().split()))
array = []
array.append(x)
array.append(y)
array.append(w-x)
array.append(h-y)
print(min(array))
