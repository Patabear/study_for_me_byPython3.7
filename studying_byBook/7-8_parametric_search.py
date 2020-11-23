# 파라메트릭 서치 by binary search
# 최적화문제를 결정문제로 바꾸어 해결하는 기법 (결정문제 =  예 아니오 답하는 문제)
# ex) 범위내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진탐색으로 결정문제를 해결하면서 범위를 좁혀갈 수 있다.

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    # print(mid)

        start = mid + 1
print(result)