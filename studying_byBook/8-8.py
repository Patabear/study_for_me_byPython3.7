# 내코드
# n, m = map(int, input().split())
# arr = list()
# d = [0] * 10000

# for i in range(n):
#     arr.append(int(input()))
#     d[arr[i]] = 1

# for i in range(arr[n-1]+1, m+1):
#     for j in arr:
#         if d[i-j] != 0:
#             if d[i] != 0:
#                 d[i] = min(d[i], d[i-j] + 1)
#             else:
#                 d[i] = d[i-j] + 1

# if d[m] != 0:
#     print(d[m])
# else:
#     print(-1)
    
# 책코드
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])