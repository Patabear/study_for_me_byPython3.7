t = int(input())

for i in range(t):
    str = input()
    arr = []
    for k in range(len(str)):
        arr.append(str[k])
    count = 0
    for j in range(len(arr)):
        if arr[j] == '(':
            count = count + 1
        elif arr[j] == ')':
            count = count - 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')
            
