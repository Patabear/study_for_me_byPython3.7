N, M = map(int, input().split())
frame = []
for i in range(N):
    frame.append(list(map(int, input())))

print(frame)
    
def checkIce(x, y):
    global frame

    if x <= -1 or x >= N or y <= -1 or y >=M:
        return False

    if frame[x][y] == 0:
        frame[x][y] = 1
        checkIce(x-1, y)
        checkIce(x, y-1)
        checkIce(x+1, y)
        checkIce(x, y+1)
        return True

count = 0
for i in range(N):
    for j in range(M):
        if checkIce(i, j) == True:
            count += 1
            
print(count)
 
   