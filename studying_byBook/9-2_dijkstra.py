# 개선된 다익스트라 알고리즘 O(ElogV) - 힙 사용
# 9-1 에서 get_smallest_node를 일반적인 순회가 아닌 최소힙을 사용

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)                      # 무한을 의미하는 값

n, m = map(int, input().split())    # 노드개수 간선개수
start = int(input())                # 시작노드
graph = [[] for i in range(n+1)]    # 간선리스트
distance = [INF] * (n+1)            # 최단거리테이블 초기화

for _ in range(m):                  # 간선정보 입력
    a,b,c = map(int, input().split())
    graph[a].append((b,c))          # a -> b, cost = c

def dijkstra(start):
    # 시작노드
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


