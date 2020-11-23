# 간단한 다익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)                      # 무한을 의미하는 값

n, m = map(int, input().split())    # 노드개수 간선개수
start = int(input())                # 시작노드
graph = [[] for i in range(n+1)]    # 간선리스트
visited = [False] * (n+1)           # 방문여부 리스트
distance = [INF] * (n+1)            # 최단거리테이블 초기화

for _ in range(m):                  # 간선정보 입력
    a,b,c = map(int, input().split())
    graph[a].append((b,c))          # a -> b, cost = c

def get_smallest_node():            # 미방문 노드중 최단거리가 짧은 노드 번호 반환
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    # 최단거리 짧은노드꺼내 확인
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


