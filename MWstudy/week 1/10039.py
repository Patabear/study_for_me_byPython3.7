total = 0
for i in range(5):
    temp = int(input())
    total = total + max(40, temp)
answer = total / 5
print(int(answer))
