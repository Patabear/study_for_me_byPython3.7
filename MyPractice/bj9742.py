count = 0
tgtCNT = 0
src = []
tgt = []
fact = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
select = []

def perm (tgtIdx) :
    if tgtIdx == srcLeng :
        global count
        count += 1
        if count == tgtCNT :
            for x in tgt :
                print(x, end='')
            print()
        return
    
    for i in range(srcLeng) :
        global select
        if select[i] :
            continue

        tgt.append(src[i])
        select[i] = True
        perm(tgtIdx+1)
        tgt.pop(-1)
        select[i] = False

while True:
    inputStream = input()
    problem, tgt = inputStream.split()
    count = 0
    tgtCNT = int(tgt)
    src = list(problem)
    srcLeng = len(src)
    tgt = []
    select = [False for i in range(srcLeng)]

    print(inputStream + " = ", end = "")

    if tgtCNT <= fact[srcLeng]:
        perm(0)
    else :
        print("No permutation")