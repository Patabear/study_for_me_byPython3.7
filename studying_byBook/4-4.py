N, M = map(int, input().split())
A, B, D = map(int, input().split())
array = [[0] * M for _ in range(N)]

for i in range(N):
    array[i] = list(map(int, input().split()))

steps = [ (0,-1), (1,0), (0,1), (-1,0) ]

def checkLand(nextX, nextY):
    global N
    global M
    global array
    if 0 <= nextX <= M-1 and 0 <= nextY <= N-1:
        if array[nextY][nextX] == 1:
            return False
        else:
            return True
    else:
        return False

cannotmove = 0
count = 1

while True:

    D += 1
    D = D % 4

    nextX = steps[D][0] + A
    nextY = steps[D][1] + B
    
    if checkLand(nextX, nextY) == False:
        cannotmove += 1
        if cannotmove == 4:
            back = (D + 2) % 4
            nextX = steps[back][0] + A
            nextY = steps[back][1] + B
            if checkLand(nextX, nextY) == False:
                break
            else:
                array[B][A] = 1
                A = nextX
                B = nextY
                cannotmove = 0
                count += 1
                continue
    else:
        array[B][A] = 1
        A = nextX
        B = nextY
        cannotmove = 0
        count += 1
        continue

print(count)



    