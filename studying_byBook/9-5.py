# 262페이지 문제풀이
# 다익스트라 응용문제

import heapq

INF = int(1e9)

n, m, c = map(int, input().split())     # c = start point

graph = [ [] for i in range(n+1) ]
distance = [INF] * (n+1)

for i in range(nm:
    x, y, z = map(int, input().split())
    graph[x].append((y,z))              # x -> y, cost = z

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
    
