n = int(input())
route = list(input().split())

x = 1
y = 1

for direction in route:
    if direction == 'R':
        if y < n:
            y += 1
    elif direction == 'L':
        if 1 < y:
            y -= 1
    elif direction == 'U':
        if 1 < x:
            x -= 1
    elif direction == 'D':
        if x < n:
            x += 1

print(x, y)