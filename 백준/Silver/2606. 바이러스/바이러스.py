from collections import deque

def bfs(v):
    visited[v] = True
    q = deque([v])

    while q:
        c = q.popleft()
        for next in graph[c]:
            if visited[next] == False:
                q.append(next)
                visited[next] = True

def dfs(v):
    visited[v]=True
    for next in graph[v]:
        if visited[next] == False:
            dfs(next)

    
if __name__ == '__main__':
    n = int(input())
    v = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)

    for _ in range(v):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    # graph [[], [2,5], [1,3,5], [2], [7], [1,2,6], [5], [4]]

    bfs(1)
    print(sum(visited)-1)
