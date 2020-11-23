n, m = map(int, input().split())
array = list(map(int, input().split()))

h = max(array)
sum = 0

while(sum < m):
    temp = (m-sum) // n
    if temp == 0:
        h = h - 1 
    else:   
        h = h - temp

    sum = 0
    for i in array:
        if i > h:
            sum = sum + i - h

    #print(sum)

print(h)