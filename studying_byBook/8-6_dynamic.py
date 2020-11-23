# top-down
# n = int(input())
# house = list(map(int, input().split()))

# def rob_house(tail):
#     if tail == 1:
#         if house[0] > house[1]:
#             return house[0]
#         else:
#             return house[1]
#     elif tail == 0:
#         return house[0]
#     elif rob_house(tail-1) > house[tail] + rob_house(tail-2):
#         return rob_house(tail-1)
#     else:
#         return house[tail] + rob_house(tail-2)

# print(rob_house(n-1))


# bottom-up
n = int(input())
house = list(map(int, input().split()))

d = [0] * 100

d[0] = house[0]
d[1] = max(house[0], house[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + house[i])

print(d[n-1])