N = int(input())
Array = list(map(int, input().split()))
M = max(Array)
average = 0

for i in range(0, len(Array)):
    Array[i] = Array[i]/M*100
    average += Array[i]

print(average/len(Array))
